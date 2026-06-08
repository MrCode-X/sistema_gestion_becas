from rest_framework import viewsets, permissions
from .models import ProgramaBeca
from .serializers import ProgramaBecaSerializer

class ProgramaBecaViewSet(viewsets.ModelViewSet):
    queryset = ProgramaBeca.objects.all()
    serializer_class = ProgramaBecaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]