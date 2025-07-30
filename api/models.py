from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

# Create your models here.
class Comprobante(models.Model):
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    class CategoryChoices(models.TextChoices):
        ALIMENTOS = 'Alimentos'
        BEBIDAS = 'Bebidas'
        HOGAR = 'Hogar'
        CUIDADO_PERSONAL = "Cuidado Personal"
        OTROS = "Otros"

    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices    
    )

    comprobante = models.ForeignKey(Comprobante, related_name="Items", on_delete=models.CASCADE)


