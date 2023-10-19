from django.urls import path, re_path
from calc import views

urlpatterns = [
    path('', views.index, name='index'),
]