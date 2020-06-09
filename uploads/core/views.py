from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from uploads.core.models import Document
from uploads.core.forms import DocumentForm

##************VERSION**************##
#VERSION 0.0.1
#UPDATED JUNE 2020
#MIT LICENSED

def readthedocs(request): #this allows the code to render the readthedocs.html file
    return render(request, 'core/readthedocs.html')

def plotfile(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plotfile.html')

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })
