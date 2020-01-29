from django.urls import path
from . import views

urlpatterns = [
    path('', views.samples_list, name='samples_list'),
    path('sample/<int:pk>/', views.sample_detail, name='sample_detail'),
]