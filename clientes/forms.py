from django import forms # type: ignore
from .models import Cliente

class ConsultaCreditoForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'sexo', 'regiao', 'estado_civil', 'numero_filhos', 'propriedade', 'educacao', 'vinculo_empregaticio', 'fonte_renda']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'regiao': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'numero_filhos': forms.Select(attrs={'class': 'form-control'}),
            'propriedade': forms.Select(attrs={'class': 'form-control'}),
            'educacao': forms.Select(attrs={'class': 'form-control'}),
            'vinculo_empregaticio': forms.Select(attrs={'class': 'form-control'}),
            'fonte_renda': forms.Select(attrs={'class': 'form-control'}),
        }
