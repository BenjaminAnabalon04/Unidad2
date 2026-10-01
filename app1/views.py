from django.shortcuts import render

def catalogo(request):
    return render(request, 'app1/catalogo.html')
