from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvando meus dados no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #mostrando os usuarios cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request,'usuarios/usuarios.html',usuarios)

