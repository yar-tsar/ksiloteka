from django.contrib import admin
from .models import Sample
from .models import Department
from .models import PickupLocation

admin.site.register(Department)
admin.site.register(PickupLocation)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('latin', 'family', 'genus', 'department', 'location', 'count')
    list_filter = ('department', 'location')
    
admin.site.register(Sample, SampleAdmin)