from django.db import models

# Create your models here.

class Producto(models.Model):
    cod_pro = models.AutoField(primary_key=True)
    nom_pro = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    stock = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f"Producto {self.cod_pro} {self.nom_pro} {self.desc} {self.stock} {self.precio}"

class Usuario(models.Model):
    nom_usr = models.CharField(primary_key=True,max_length=10)
    nom = models.CharField(max_length=50)
    ape = models.CharField(max_length=50)
    dni = models.IntegerField()
    tel = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"Usuario {self.nom_usr} {self.nom} {self.ape} {self.dni} {self.tel} {self.email}"

class Compra(models.Model):
    cod_compra = models.AutoField(primary_key=True)
    cod_pro = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cant = models.IntegerField()
    nom_usr = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Compra {self.cod_compra} {self.cod_pro} {self.cant} {self.monto} {self.nom_usr}"