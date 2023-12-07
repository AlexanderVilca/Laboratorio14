from .views import registrar_empleado, listar_empleados
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet, basename='empleado')

urlpatterns = [
    path('', include(router.urls)),
    path('registrar/', registrar_empleado, name='registrar_empleado'),
    path('listar/', listar_empleados, name='listar_empleados'),
]
