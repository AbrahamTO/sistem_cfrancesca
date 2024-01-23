from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import Shoesform
from .models import zapatos  
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('shoes')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error':'Ya existe el trabajador' } )
    
        return render(request, 'signup.html', {'form': UserCreationForm, 'error':'Las contraseñas no coinciden' } ) #RETORNA EL FORMULARIO PERO AGREGANDO EL ERROR
@login_required    
def shoes(request):
    zapatoss= zapatos.objects.all().order_by('-codigo') 
    return render(request, 'shoes.html',{'zapatos':zapatoss})
@login_required   
def shoes_sold(request):
    zapatoss= zapatos.objects.filter(fecha_vendida__isnull=False).order_by('-fecha_vendida')  
    return render(request, 'shoes.html',{'zapatos':zapatoss}) 
@login_required   
def create_shoes(request):
    if request.method == 'GET':
        return render(request, 'create_shoes.html', {'form': Shoesform})
    else:
        try:
            form = Shoesform(request.POST)
            nuevo_zapato = form.save(commit=False)
            nuevo_zapato.user = request.user
            nuevo_zapato.save()
            return redirect('shoes')
        except ValueError:
            return render(request, 'create_shoes.html', {'form': Shoesform, 'error': 'Error al crear, valide datos'})
@login_required   
def edit_shoes(request, zapato_codigo):
    if request.method=='GET':
        zapato= get_object_or_404(zapatos, pk=zapato_codigo)
        form= Shoesform(instance=zapato)
        return render(request, 'edit_shoes.html', {'zapato': zapato, 'form':form})
    else:
        try:
            zapato=get_object_or_404(zapatos, pk=zapato_codigo)
            form= Shoesform(request.POST, instance=zapato)
            form.save()
            return redirect('shoes')
        except ValueError:
            return render(request, 'edit_shoes.html', {'zapato': zapato, 'form':form, 'error': 'Error al actualizar los datos'})
@login_required   
def sold_shoes(request,zapato_codigo):
    zapato= get_object_or_404(zapatos, pk=zapato_codigo)
    if request.method == 'POST':
        zapato.fecha_vendida= timezone.now()
        zapato.save()
        return redirect('shoes')
@login_required               
def delete_shoes(request,zapato_codigo):
    zapato= get_object_or_404(zapatos, pk=zapato_codigo)
    if request.method == 'POST':
        zapato.delete()
        return redirect('shoes')
    
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form':AuthenticationForm})
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form':AuthenticationForm, 'error':'Usuario o contraseña incorrecta'})
        else:
            login(request, user)
            return redirect('shoes')
        
    

