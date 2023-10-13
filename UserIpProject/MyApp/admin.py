from django.contrib import admin

# Register your models here.

from .models import UserIp, UserIpLocation

admin.site.register(UserIp)
admin.site.register(UserIpLocation)


