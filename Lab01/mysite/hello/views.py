import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1 style="color:#2b5797; font-size: 32px;">Welcome to my Django application.</h1>')


def fancy_index(request):
    return render(request, "hello/index.html")


def hello_name(request, name):
    data = {
        'name': name.capitalize(),
        'time': datetime.datetime.now(),
        'show_time': True
    }
    return render(request, "hello/greet.html", data)
