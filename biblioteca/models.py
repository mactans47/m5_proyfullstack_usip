from django.db import models
from .validators import validation_isbn
from django.utils import timezone

# Create your models here.
class Editorial(models.Model):
    nombre=models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    isbn=models.CharField(max_length=20, unique=True, validators=[validation_isbn])
    titulo=models.CharField(max_length=200)
    autor=models.CharField(max_length=200)
    anio=models.IntegerField(default=0)
    editorial=models.ForeignKey(Editorial,null=False,blank=False,on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
class Persona(models.Model):
        apellido_paterno=models.CharField(max_length=25,verbose_name='Apellido Paterno')
        apellido_materno=models.CharField(max_length=25,verbose_name='Apellido Materno')
        nombres=models.CharField(max_length=50,verbose_name='Nombres')
        telefono=models.CharField(max_length=10)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def nombre_completo (self):
            return "{},{},{},{}".format(self.apellido_paterno,self.apellido_materno,self.nombres,self.telefono)

        def __str__(self):
                return self.nombre_completo()
    
class Prestamo(models.Model):
        descripcion=models.TextField()
        persona=models.ForeignKey(Persona,null=False,blank=False,on_delete=models.CASCADE)
        libro=models.ForeignKey(Libro,null=False,blank=False,on_delete=models.CASCADE)
        fecha=models.DateField(auto_now_add=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def prestamo_libro (self):
            return "{},{},{}".format(self.persona,self.libro,self.fecha)

        def __str__(self):
            return self.prestamo_libro()