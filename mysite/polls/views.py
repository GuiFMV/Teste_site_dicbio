from django.shortcuts import render


def home_view(request):
    images = [
        'polls/images/brotero_img.svg',
        'polls/images/conchas_img.svg',
        'polls/images/flora_img.svg',
        'polls/images/flora2_img.svg',
        'polls/images/flora3_img.svg'
    ]
    return render(request, 'polls/home.html', {'images': images})

def consulta_view(request):

    return render(request, 'polls/consulta.html')


def documentacao_view(request):
    return render(request, 'polls/documentacao.html')


def curiosidades_view(request):
    return render(request, 'polls/curiosidades.html')
