from django.shortcuts import render,redirect,get_object_or_404
from .models import Usuarios,Posts,Planes
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):

    usuarios = Usuarios.objects.all()
    return render(request, "gestionUsuarios.html",{"Users" : usuarios})

def registrarUsuario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    clave=request.POST['txtClave']

    Usuario = Usuarios.objects.create(codigo=codigo,nombre=nombre,clave=clave)
    return redirect('/')



def eliminacionUsuario(request,codigo):
    Usuario = Usuarios.objects.get(codigo=codigo)
    Usuario.delete()
    return redirect('/')

def edicionUsuario(request,codigo):
    Usuario = get_object_or_404(Usuarios, codigo=codigo)
    return render(request,"edicionUsuario.html",{"Usuario": Usuario})

def editarUsuario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    clave=request.POST['txtClave']

    Usuario = Usuarios.objects.get(codigo=codigo)
    Usuario.nombre = nombre
    Usuario.clave = clave
    Usuario.save()
    return redirect('/')
def Panoramas(request):

    return render(request, "Panoramas.html")

def Novedades(request):

    return render(request, "Novedades.html")

def Post(request):
    postlistado = Posts.objects.all()
    return render(request,"gestionPost.html",{"Posts": postlistado})


def eliminacionPost(request, id):
    post = get_object_or_404(Posts, id=id)
    post.delete()
    return redirect('/Posts/')



def registrarPost(request):
    if request.method == "POST":
        username = request.POST['post-username']
        text = request.POST['post-text']
        image_url = request.POST.get('post-image-url', '')
        post = Posts.objects.create(username=username, text=text, image_url=image_url)
        response_data = {
            'id': post.id,
            'username': post.username,
            'text': post.text,
            'image_url': post.image_url,
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        return JsonResponse(response_data)
    return render(request, 'registrarPost.html')
    

def posts_view(request):
    posts = Posts.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})


def carrito(request):
    planes = Planes.objects.all()
    return render(request, "carrito.html",{"planes" : planes})


def eliminacionPlan(request,codigo):
    planes = get_object_or_404(Planes, codigo=codigo)
    planes.delete()
    return redirect('/carrito/')


def registrarPlan(request):
    codigo=request.POST['txtCodigo']
    email=request.POST['txtEmail']

    Plan = Planes.objects.create(codigo=codigo,email=email)
    return redirect('/carrito/')
