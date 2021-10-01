from django.contrib import admin

# Register your models here.
from tutorialSLMApp.models import Contenido,Categoria,SubCategoria
admin.site.register(Contenido)
admin.site.register(Categoria)
admin.site.register(SubCategoria)