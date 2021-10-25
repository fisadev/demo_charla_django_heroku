from django.db import models


class Opcion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Respuesta(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)

    @classmethod
    def totales(cls):
        return {
            datos_opcion["opcion"]: datos_opcion["total"]
            for datos_opcion in cls.objects.all().values('opcion')\
                                                 .annotate(total=models.Count('opcion'))
        }

