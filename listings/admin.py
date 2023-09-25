from django.contrib import admin
from .models import *
from .forms import PoiForm
# Register your models here.

class PoiAdmin(admin.ModelAdmin):
    form = PoiForm
    
admin.site.register(Listings)
admin.site.register(Poi, PoiAdmin)
