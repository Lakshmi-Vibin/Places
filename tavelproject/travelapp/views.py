from django.http import HttpResponse
from django.shortcuts import render

from .models import Place, Guides


# Create your views here.
# def demo(request):
#     return HttpResponse("This is my First Django project")


def home(request):
    obj = Place.objects.all()
    obj2 = Guides.objects.all()
    return render(request, "indexx.html", {'result': obj, 'guides': obj2})


def about(request):
    return render(request, "home.html")
