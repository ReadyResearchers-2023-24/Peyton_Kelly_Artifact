from django.contrib import admin
from .models import Record , Monitor, CPU_load


# Register your models here.

admin.site.register(Record)
admin.site.register(Monitor)
admin.site.register(CPU_load)