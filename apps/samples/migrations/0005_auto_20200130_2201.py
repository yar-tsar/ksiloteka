# Generated by Django 3.0.2 on 2020-01-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0004_auto_20200130_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickuplocation',
            name='name',
            field=models.CharField(choices=[('Беларусь', 'Беларусь'), ('Россия', 'Россия'), ('Чехия', 'Чехия'), ('Румыния', 'Румыния'), ('США', 'США')], default='Беларусь', max_length=20),
        ),
    ]
