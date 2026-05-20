from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    lista_users = [
        {"nome": "João", "matricula": 18, "idade": 17, "cidade": "São Paulo do Potengi"},
        {"nome": "Lopetegui", "matricula": 222, "idade": 69, "cidade": "Lagoa de Velhos"},
        {"nome": "Ayhan", "matricula": 333, "idade": 17, "cidade": "Lagoa de Fora"},
        {"nome": "José", "matricula": 444, "idade": 17, "cidade": "São Tomé"},
        {"nome": "Neymar", "matricula": 10, "idade": 34, "cidade": "Santos"},
    ]

    context = {
        "usuarios": lista_users,
    }
    
    return render(request, "usuarios.html", context)