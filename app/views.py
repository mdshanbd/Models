from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician,Album
# Create your views here.

def home(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {
        'text_1': 'THIS IS A LIST OF MUSICIANS',
        'musician': musician_list
    }
    return render(request, 'index.html', context=diction)
