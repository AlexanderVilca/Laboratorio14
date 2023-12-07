from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    horas_trabajadas = models.IntegerField()
    pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calcular_pago(self):
        if self.categoria == 'A':
            return 30 * self.horas_trabajadas
        elif self.categoria == 'B':
            return 20 * self.horas_trabajadas
        elif self.categoria == 'C':
            return 10 * self.horas_trabajadas
        else:
            return 0
        
    def save(self, *args, **kwargs):
        self.pago = self.calcular_pago()
        super().save(*args, **kwargs)
