from django.db import models

# Create your models here.
class Cuarto(models.Model):
  number = models.IntegerField()
  available = models.BooleanField('Disponible', default=False)
  description = models.TextField()
  price = models.FloatField()
  fecha_pago = models.DateField(null=True)