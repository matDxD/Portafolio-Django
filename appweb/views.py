from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hola mundoi")
    return render(request, 'marvel/index.html')