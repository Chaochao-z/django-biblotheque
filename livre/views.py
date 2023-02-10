from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'test.html', context={})

def libraire(request):
    return render(request, 'libraire/index.html')
