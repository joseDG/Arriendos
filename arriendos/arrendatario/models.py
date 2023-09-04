from django.db import models

#importar modelo Cuarto
from cuarto.models import Cuarto

# Create your models here.
class Arrendatario(models.Model):

  first_name = models.CharField("Nombres", max_length=50)
  last_name = models.CharField("Apellidos", max_length=50)
  full_name = models.CharField("Nombres Completos", max_length=120, blank=True)
  contact = models.CharField("Contacto", max_length=20)
  cuarto = models.ForeignKey(Cuarto, on_delete=models.CASCADE)