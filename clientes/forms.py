from django import forms # type: ignore
from .models import Cliente

class ConsultaCreditoForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'sexo', 'regiao', 'estado_civil', 'numero_filhos', 'propriedade', 'educacao', 'vinculo_empregaticio', 'fonte_renda']
        
        labels = {
            'nome': 'Name',
            'email': 'Email',
            'sexo': 'Gender',
            'regiao': 'Region',
            'estado_civil': 'Marital Status',
            'numero_filhos': 'Number of Children',
            'propriedade': 'Property Type',
            'educacao': 'Education Level',
            'vinculo_empregaticio': 'Employment Status',
            'fonte_renda': 'Income Source',
        }
        
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'regiao': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'numero_filhos': forms.Select(attrs={'class': 'form-control'}),
            'propriedade': forms.Select(attrs={'class': 'form-control'}),
            'educacao': forms.Select(attrs={'class': 'form-control'}),
            'vinculo_empregaticio': forms.Select(attrs={'class': 'form-control'}),
            'fonte_renda': forms.Select(attrs={'class': 'form-control'}),
        }
