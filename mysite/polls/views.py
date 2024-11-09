from django.shortcuts import render


def home_view(request):
    return render(request, 'polls/home.html')


def consulta_view(request):
    return render(request, 'polls/consulta.html')


def documentacao_view(request):
    return render(request, 'polls/documentacao.html')


def curiosidades_view(request):
    return render(request, 'polls/curiosidades.html')
