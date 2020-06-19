from django.shortcuts import render
from shoedata.models import Shoe
# Create your views here.

def index(request):
    shoedata = Shoe.objects.all()
    return render(request, 'index.html', {'shoedata': shoedata})

