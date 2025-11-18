from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-field',
        'placeholder': 'Digite sua senha'
    }))

    role = forms.ChoiceField(
        choices=[
            ('superadmin', 'Admin'),
            ('editor', 'Editor de Conteúdo'),
            ('viewer', 'Visualizador')
        ],
        widget=forms.Select(attrs={'class': 'input-field'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Digite seu nome completo'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'input-field',
                'placeholder': 'Digite seu e-mail'
            }),

            'username': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Digite o login'
            }),
        }
