from django.db import models
from django.conf import settings


class Sample(models.Model):
    # list of countries for location 
    BELARUS = 'Беларусь'
    RUSSIA = 'Россия'
    CZECH = 'Чехия'
    ROMANIA = 'Румыния'
    USA = 'США'
    CAMBODIA = 'Камбоджа'

    LOCATION_CHOICES =(
    (BELARUS, 'Беларусь'),
    (RUSSIA, 'Россия'),
    (CZECH, 'Чехия'),
    (ROMANIA, 'Румыния'),
    (USA, 'США'),
    (CAMBODIA, 'Камбоджа'),)
    latin = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    genus = models.CharField(max_length=50)
    location = models.CharField(
        max_length=20,
        choices = LOCATION_CHOICES,
        default = BELARUS
    )
    bio = models.TextField()
    # photo = models.ImageField(blank=True, upload_to='media/wood/')


    def publish(self):
        self.save()

    def __str__(self):
        return self.name