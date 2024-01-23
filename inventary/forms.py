from django import forms
from .models import zapatos

class Shoesform(forms.ModelForm):
    class Meta:
        model= zapatos
        fields=[
                'color',
                'talla',
                'modelo',
                'caracteristicas',
                'taco',
                'categoria',
                'precio',]
        widgets={
                'color': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingrese el color'}),
                'talla': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingrese la talla'}),
                'modelo': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingrese el modelo'}),
                'caracteristicas': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingrese las características (opcional)'}),
                'taco': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingrese el número de taco'}),
                'categoria': forms.Select(attrs={'class': 'form-control mb-2'},
                                choices=[('Varón', 'Varón'), ('Mujer', 'Mujer')]),
                'precio': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingrese el precio'}), }
        
