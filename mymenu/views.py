from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def hello(request):
    return render(request, 'named_url.html')


def world(request, pk: int):
    return render(request, 'named_url.html', context={'pk': pk})
