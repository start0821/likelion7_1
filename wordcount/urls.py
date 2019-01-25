from . import views
from django.urls import path

app_name = 'wordcount'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('result',views.result, name='result'),
]