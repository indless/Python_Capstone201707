from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, you are at the findjobs index.")

# Create your views here.
