from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Campos já existentes no AbstractUser:
    # username -> será o "login"
    # first_name -> nome
    # last_name -> sobrenome
    # email
    # password -> senha

    NIVEL_CHOICES = (
        ("admin", "Administrador"),
        ("func", "Funcionário"),
        ("user", "Usuário Comum"),
    )

    nivel_acesso = models.CharField(
        max_length=20,
        choices=NIVEL_CHOICES,
        default="user"
    )

    def __str__(self):
        return f"{self.username} ({self.nivel_acesso})"

