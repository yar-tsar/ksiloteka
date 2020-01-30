from django.shortcuts import render
from .models import Sample
from .models import Department
from .models import PickupLocation
from django.shortcuts import render, get_object_or_404

def sample_detail(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    return render(request, 'samples/sample_detail.html', {'sample': sample})

def samples_list(request):
    posts = Sample.objects.order_by('latin')
    return render(request, 'samples/samples_list.html', {'posts': posts})
