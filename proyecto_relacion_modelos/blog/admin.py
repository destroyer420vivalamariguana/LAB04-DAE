from django.contrib import admin

# Register your models here.

from .models import Autor, Entrada 
 
admin.site.register(Autor) 
admin.site.register(Entrada) 