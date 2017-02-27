from django.shortcuts import render

__author__ = 'yves'

def home(request):

    return render(request, "index.html", {"": ""})