from rest_framework import serializers
from .models import Postulacion
from apps.programas.models import ProgramaBeca
from apps.estudiantes.models import Estudiante

class PostulacionSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.CharField(source='estudiante.nombre_completo', read_only=True)
    programa_nombre = serializers.CharField(source='programa.nombre', read_only=True)
    
    class Meta:
        model = Postulacion
        fields = ['id', 'estudiante', 'programa', 'fecha_postulacion', 'estado', 
                  'dictamen_comite', 'monto_asignado', 'estudiante_nombre', 'programa_nombre']