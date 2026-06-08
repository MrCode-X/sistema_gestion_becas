from rest_framework import serializers
from .models import ProgramaBeca

class ProgramaBecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaBeca
        fields = '__all__'