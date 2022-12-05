from django.shortcuts import render
from .models import Car

def car( request):
    cars = Car.objects.all()
    moshina = {
        'cars': cars
    }
    return render(request, 'index.html', moshina)

