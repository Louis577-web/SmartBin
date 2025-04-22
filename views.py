from django.http import HttpResponse
from django.shortcuts import render
def Accueil_view(request):
    return render(request,'Accueil.html')
def contact_view(request):
    return render(request,'contact.html')