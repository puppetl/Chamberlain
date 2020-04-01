from django.shortcuts import render
from django.http import HttpResponse
from hotel.models import Article

# Create your views here.

def home(request):
    first_article = Article.objects.all()
    return render(request, 'home_reservation.html',{
        'article': first_article,
    })

def leisure(request):
    first_article = Article.objects.all()
    return render(request, 'home_reservation.html',{
        'article': first_article,
    })