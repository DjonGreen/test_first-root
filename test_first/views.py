from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('<h1>Вот так вот</h1>')

def home(request):
    return render(request, 'home.html', {'greeting': 'Hello!'})

def feedback(request):
    return render(request, 'feedback.html')

def reverse(request):
    user_text = request.GET['usertext']
    print(user_text)
    reverse_user_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'reversetext': reverse_user_text})
