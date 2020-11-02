from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Direccion(models.Model):
    region= models.CharField(max_length=50)
    comuna= models.CharField(max_length=50)
    calle= models.CharField(max_length=50)


class Usuario(models.Model):
    rut= models.CharField(max_length=12)
    direccion= models.ForeignKey(Direccion, on_delete=models.CASCADE)
    usuario= models.OneToOneField(User, on_delete=models.CASCADE)