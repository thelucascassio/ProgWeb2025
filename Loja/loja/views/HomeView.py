#from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    #return HttpResponse('<h1>Olá mundo!</h1>')
    return render(request, template_name='home/home.html', status=200)
