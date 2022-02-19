from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('<h1>Вот так вот</h1>')

def home(request):
    return render(request, 'home.html', {'greeting': 'Hello!'})

def feedback(request):
    return render(request, 'feedback.html')