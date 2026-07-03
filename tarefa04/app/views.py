from django.shortcuts import render
from . models import Tarefa
from datetime import date


def index(request):
    tarefas = Tarefa.objects.all()
    context = {
       "tarefas": tarefas,
       "hoje": date.today(),
    }
    return render(request, "app/index.html", context)