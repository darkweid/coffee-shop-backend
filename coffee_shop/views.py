from django.shortcuts import render
from django.http import HttpResponse

# Представление для домашней страницы
def home(request):
    return HttpResponse("<h1>Welcome to Coffee Shop!</h1>")
