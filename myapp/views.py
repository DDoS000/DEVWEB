from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl

# from .models import Service

# Create your views here.
def index(req):
    return render(req, 'myapp/index.html')
