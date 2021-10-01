from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Categoria(models.Model):
     titulo = models.CharField(max_length=200)
     sobre=models.TextField(null=True,blank=True )
     def __str__(self):
            return self.titulo


class SubCategoria(models.Model):
    titulo = models.CharField(max_length=200)
    categoriaC = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True,blank=True  )
    def __str__(self):
        return self.titulo
#comentario
class Contenido(models.Model):
      titulo = models.CharField(max_length=200)
      cuerpo = RichTextField()
      fecha_publicacion = models.DateField()
      video=models.FileField(upload_to='videos')
      categoriaC =models.ForeignKey(Categoria, on_delete=models.CASCADE,)
      SubcategoriaC = models.ForeignKey(SubCategoria, on_delete=models.CASCADE,null=True,blank=True )
      usuario= models.CharField(max_length=200,null=True,blank=True)
      def __str__(self):
            return self.titulo

