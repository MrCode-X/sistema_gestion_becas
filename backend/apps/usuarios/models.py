from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('comite', 'Comité de Becas'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='comite')
    
    def __str__(self):
        return f"{self.username} ({self.role})"