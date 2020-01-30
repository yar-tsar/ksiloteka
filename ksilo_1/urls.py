from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('samples/', include('apps.samples.urls')),
    path('', RedirectView.as_view(url='/samples/', permanent=True)),
]
