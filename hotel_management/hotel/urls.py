from django.urls import path
from hotel import views
urlpatterns = [
    path('hello/', views.home),
]