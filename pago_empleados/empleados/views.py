from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Empleado
from .forms import EmpleadoForm
from .serializers import EmpleadoSerializer
from rest_framework import viewsets


def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()

    return render(request, 'empleados/registrar_empleado.html', {'form': form})

def listar_empleados(request):
    empleados = Empleado.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = [{'nombre': emp.nombre, 'categoria': emp.categoria, 'horas_trabajadas': emp.horas_trabajadas, 'pago': emp.calcular_pago()} for emp in empleados]
        return JsonResponse(data, safe=False)
    else:
        return render(request, 'empleados/listar_empleados.html', {'empleados': empleados})

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer