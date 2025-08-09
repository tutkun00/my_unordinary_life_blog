from django.shortcuts import render
from django.http import HttpResponse


def homePage(req):
    return render(req, 'index.html')
