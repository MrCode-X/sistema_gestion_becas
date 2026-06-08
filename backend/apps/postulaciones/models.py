from django.db import models
from apps.programas.models import ProgramaBeca
from apps.estudiantes.models import Estudiante

class Postulacion(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
       ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    )
    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='postulaciones')
    programa = models.ForeignKey(ProgramaBeca, on_delete=models.CASCADE, related_name='postulaciones')
    fecha_postulacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    dictamen_comite = models.TextField(blank=True, null=True)
    monto_asignado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.estudiante.nombre_completo} - {self.programa.nombre} ({self.estado})"