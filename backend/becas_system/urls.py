from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView

from apps.programas.views import ProgramaBecaViewSet
from apps.estudiantes.views import EstudianteViewSet
from apps.postulaciones.views import PostulacionViewSet

router = DefaultRouter()
router.register(r'programas', ProgramaBecaViewSet)
router.register(r'estudiantes', EstudianteViewSet)# Agrega la ruta para postulaciones
router.register(r'postulaciones', PostulacionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', TemplateView.as_view(template_name='index.html')),
]