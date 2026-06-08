from django.db import models

class Estudiante(models.Model):
    ci = models.CharField(max_length=15, unique=True)
    nombre_completo = models.CharField(max_length=200)
    email = models.EmailField()
    carrera = models.CharField(max_length=100)
    semestre = models.IntegerField()
    promedio = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.nombre_completo} - {self.carrera}"