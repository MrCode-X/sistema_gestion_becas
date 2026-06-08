from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum, Avg
from .models import Postulacion
from .serializers import PostulacionSerializer

class PostulacionViewSet(viewsets.ModelViewSet):
    queryset = Postulacion.objects.all()
    serializer_class = PostulacionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # ✅ Consulta 1: Postulaciones por estado
    @action(detail=False, methods=['get'])
    def por_estado(self, request):
        estado = request.query_params.get('estado', 'pendiente')
        postulaciones = Postulacion.objects.filter(estado=estado)
        serializer = self.get_serializer(postulaciones, many=True)
        return Response(serializer.data)
    
    # ✅ Consulta 2: Becas aprobadas por programa
    @action(detail=False, methods=['get'])
    def resumen_por_programa(self, request):
        resumen = Postulacion.objects.filter(estado='aprobada').values('programa__nombre').annotate(
            total=Count('id'),
            monto_total=Sum('monto_asignado')
        )
        return Response(resumen)
    
    # ✅ Consulta 3: Estudiantes con promedio mayor a X
    @action(detail=False, methods=['get'])
    def estudiantes_destacados(self, request):
        promedio_min = request.query_params.get('promedio_min', 80)
        destacados = Postulacion.objects.filter(
            estudiante__promedio__gte=promedio_min,
            estado='aprobada'
        ).select_related('estudiante').values(
            'estudiante__nombre_completo',
            'estudiante__promedio',
            'programa__nombre'
        )
        return Response(destacados)
    
    # ✅ Consulta 4: Inversión total por año
    @action(detail=False, methods=['get'])
    def inversion_total(self, request):
        total = Postulacion.objects.filter(estado='aprobada').aggregate(
            total_invertido=Sum('monto_asignado')
        )
        return Response(total)
    
    # ✅ Consulta 5: Programas con más postulaciones
    @action(detail=False, methods=['get'])
    def ranking_programas(self, request):
        ranking = Postulacion.objects.values('programa__nombre').annotate(
            total_postulaciones=Count('id')
        ).order_by('-total_postulaciones')[:5]
        return Response(ranking)