from django.shortcuts import render
from django.http import Response

# Create your views here.
def index(request):
    return "Hello-world from django"