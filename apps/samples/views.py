from django.shortcuts import render
from .models import Sample

def samples_list(request):
    posts = Sample.objects.order_by('latin')
    return render(request, 'samples/samples_list.html', {'posts': posts})
