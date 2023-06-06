from django.urls import path

from . import views

app_name = 'algo'
urlpatterns = [
    path('', views.form_send, name='form_send'),
    path('form_result/', views.form_result, name='form_result'),
    path('table/', views.table, name='table'),
]
