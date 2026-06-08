from django.db import models

class ProgramaBeca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    plazas = models.IntegerField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre