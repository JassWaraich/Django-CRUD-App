from django.contrib import admin

# Register your models here.
from .models import Availstatic

# django-administration for the site.
class AvailstaticAdmin(admin.ModelAdmin):
    list_display = ('row_date' , 'director', 'manager', 'analyst', 'logid',)
    list_filter = ('row_date', 'director', 'manager', 'analyst')
    date_hierarchy = 'row_date'
    ordering = ('-row_date',)
    fields = ('row_date' , 'director', 'manager', 'analyst')


admin.site.register(Availstatic,AvailstaticAdmin)