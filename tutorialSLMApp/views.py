from django.shortcuts import render
from tutorialSLMApp.models import  Contenido,SubCategoria,Categoria
# Create your views here.


def main(request):

    return render(request,'index.html')

def ayuda(request):
    id_contenido = request.GET['id_contenido']
    id_categoria = request.GET['id_categoria']
    listaCategoria = Categoria.objects.filter(pk=id_categoria)
    lista_contenido = Contenido.objects.filter(pk=id_contenido)
    subcategoria_list = SubCategoria.objects.raw('SELECT s.id,s.titulo FROM "tutorialSLMApp_contenido" t, "tutorialSLMApp_subcategoria" s where  t."categoriaC_id"='+id_categoria)
    about_list = Categoria.objects.filter(pk=id_categoria)
    return render(request,'ayuda.html', {'listaCategoria':listaCategoria,'lista_subcategoria':subcategoria_list,'about_list':about_list,'contenido_list':lista_contenido})

def listadoDeAyuda(request):
    id_contenido = request.GET['id_categoria']

    listaCategoria = Categoria.objects.filter(pk=id_contenido)
    lista_contenido = Contenido.objects.all()
    subcategoria_list = SubCategoria.objects.raw('SELECT s.id,s.titulo FROM "tutorialSLMApp_contenido" t, "tutorialSLMApp_subcategoria" s where  t."categoriaC_id"='+id_contenido)
    about_list = Categoria.objects.filter(pk=id_contenido)
    return render(request,'listado_ayuda.html', {'listaCategoria':listaCategoria,'lista_subcategoria':subcategoria_list,'about_list':about_list,'contenido_list':lista_contenido})