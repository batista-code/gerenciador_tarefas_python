from django.shortcuts import render

# Create your views here.

def listar_taferas(request):
    nome_tarefa = 'Aprendendo sobre Python e Django com a TreinaWeb'
    return render(request, 'tarefas/listar_tarefas.html', {'nome_tarefa': nome_tarefa})
