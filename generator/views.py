from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'qwerty'})


def password(request):
    length = int(request.GET.get('length'))
    if length > 1000:
        return render(request, 'generator/error.html')
    characters = string.ascii_lowercase
    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase

    if request.GET.get('symbols'):
        characters += '!@#$%^&*(){}:;",./?'

    if request.GET.get('number'):
        characters += '1234567890'

    m_password = ''

    for x in range(length):
        m_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': m_password})


def info(request):
    return render(request, 'generator/info.html')