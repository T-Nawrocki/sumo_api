from django.urls import path

from . import views

app_name = 'rikishi'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:rikishi_id>/', views.show, name='show')
]

