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

def plotmaricopa(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plotmaricopa.html')

def maricopa(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/maricopa.html')

def salt_lake(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/salt_lake.html')

def plotsalt_lake(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plotsalt_lake.html')

def utah(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/utah.html')

def plotutah(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plotutah.html')

def plotsan_diego(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plotsan_diego.html')

def san_diego(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/san_diego.html')

def plotclark(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plotclark.html')

def clark(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/clark.html')

def plottravis(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plottravis.html')

def travis(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/travis.html')

def plotwestchester(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plotwestchester.html')

def westchester(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/westchester.html')

def plotpercapita(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/plotpercapita.html')

def percapita(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/percapita.html')

def harris(request): #this allows the code to render the plotfile.html file
    return render(request, 'core/harris.html')

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })
