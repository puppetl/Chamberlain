from django.urls import path
from hotel import views

urlpatterns = [
    path('hello/', views.home),  # 主页
    path('leisure/', views.leisure),  # 空闲
    path('reservation/', views.home),  # 预订
    path('retreat/', views.home),  # 退房
]
