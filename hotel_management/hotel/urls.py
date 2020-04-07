from django.urls import path
from hotel import views

urlpatterns = [
    path('hello/', views.home, name='check'),  # 主页
    path('leisure/', views.leisure),  # 空闲
    path('reservation/', views.reservation),  # 预订
    path('retreat/', views.retreat),  # 退房
    path('people_data/', views.people_data, name='peopled_ata'),  # 信息登记
]
