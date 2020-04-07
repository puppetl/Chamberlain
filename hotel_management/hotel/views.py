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
        room_id = request.POST.get('ROOMID')
        return render(request, 'room_reservation.html', {
            'roomid': room_id,
        })


def retreat(request):  # 退房
    return render(request, 'room_unreg.html')


def people_data(request):  # 填写预订人员信息
    if request.method == 'POST':
        data_Article = Article(room_id=request.POST.get('id'), room_name=request.POST.get('name'),
                               room_timestart=request.POST.get('starttime'), room_timeover=request.POST.get('overtime'))
        data_Article.save()

