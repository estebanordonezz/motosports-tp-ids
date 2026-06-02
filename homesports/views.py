from django.shortcuts import HttpResponse, redirect, render, get_object_or_404
from .forms import MotoForm
from .models import Moto

contexto = {"nombre": "Roberto Carlos",
            "laPosee": True,
            "motos": ["Kawasaki", "Honda", "Yamaha"],
            }

def home(request):
    motos = Moto.objects.all()
    contexto = {"motos": motos}
    return render(request, "homesports/motos.html", contexto)

def index(request):
    return render(request, "homesports/index.html")

def crear_moto(request):
    if request.method == "POST":
        form = MotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MotoForm()

        return render(request, 'homesports/crear_moto.html', {'form': form})
    
def editar_moto(request, id):

    moto = get_object_or_404(Moto, id=id)

    if request.method == "POST":
        form = MotoForm(request.POST, request.FILES, instance=moto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MotoForm(instance=moto)

    return render(request, 'homesports/editar_moto.html', {'form': form})

def eliminar_moto(request, id):

    moto = get_object_or_404(Moto, id=id)

    if request.method == "POST":
        moto.delete()
        return redirect('home')

    return render(request, 'homesports/borrar_moto.html', {'moto': moto})

