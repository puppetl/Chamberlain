from django.shortcuts import render
from django.http import HttpResponse
from hotel.models import Article


# Create your views here.

def home(request):  # 主页
    first_article = Article.objects.all()
    return render(request, 'home_reservation.html', {
        'article': first_article,
    })


def leisure(request):  # 查看空闲房
    first_article = Article.objects.all()
    return render(request, 'home_reservation.html', {
        'article': first_article,
    })

def reservation(request):  # 预订
    if request.method == 'POST':
