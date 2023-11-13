from django.contrib import admin
from myapp.models import employee

# Register your models here.
class infoadmin(admin.ModelAdmin):

    list_display=("name"),
    
   
admin.site.register(employee,infoadmin)