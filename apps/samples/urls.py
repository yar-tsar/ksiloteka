from django.urls import path
from . import views

urlpatterns = [
    path('', views.samples_list, name='samples_list'),
]