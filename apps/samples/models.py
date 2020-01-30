from django.db import models
from django.conf import settings
from django.urls import reverse


class Sample(models.Model):
    latin = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50, blank=True)
    genus = models.CharField(max_length=50, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('PickupLocation', on_delete=models.SET_NULL, null=True)
    bio = models.TextField(blank=True)
    count = models.IntegerField(default=1)
    photo = models.ImageField(blank=True, upload_to='wood/')


    def get_absolute_url(self):
        return reverse('sample-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Department(models.Model):
    # list of departments
    # Cycadophyta = 'Саговниковидные'
    # Ginkgophyta = 'Гинкговидные'
    # Pinophyta = 'Хвойные'
    # Gnetophyta = 'Гнетовидные'
    # Magnoliophyta = 'Цветковые растения'

    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('department-list', args=[str(self.id)])

    def __str__(self):
        return self.name

class PickupLocation(models.Model):
    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('samples-location', args=[str(self.id)])

    def __str__(self):
        return self.name