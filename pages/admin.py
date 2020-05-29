from django.contrib import admin
from .models import *

# Register your models here.


class CalcrrAdminHS(admin.ModelAdmin):
    # list_display = ['id', 'code', 'name', 'measureCode', 'rate']
    list_display = [field.name for field in CalcHscode._meta.fields]

    class Meta:
        model = CalcHscode


class CalcrrAdminMS(admin.ModelAdmin):
    list_display = [field.name for field in CalcMeasure._meta.fields]

    class Meta:
        model = CalcMeasure



admin.site.register(CalcHscode, CalcrrAdminHS)
admin.site.register(CalcMeasure, CalcrrAdminMS)
admin.site.register(ImageSite)
