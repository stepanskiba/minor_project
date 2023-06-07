from django.urls import path

from . import views

app_name = 'atom'
urlpatterns = [
    path('', views.main, name='main'),
    path('service/', views.service, name='service'),
    path('topic/', views.topic, name='topic'),
    path('task/', views.task, name='task'),

]
