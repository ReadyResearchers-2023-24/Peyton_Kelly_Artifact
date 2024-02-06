"""
URL configuration for Admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User, Group

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from website.models import Record , Monitor

class OTPAdmin(OTPAdminSite):
   pass

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(Group)
#honeypot admin
admin_honeypot_site = admin.AdminSite(name="admin_honeypot")
admin_site.register 

admin_site.register(TOTPDevice, TOTPDeviceAdmin)

admin_site.register(Record)
admin_site.register(Monitor)



urlpatterns = [
    path("secret/", admin_site.urls),
    path("", include("website.urls")),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("hashed-shh/", admin.site.urls), #this is the default admin site that comes with django
    # currently usising admin_site instead of admin.site for 2fa 
]
