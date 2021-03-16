from django.contrib import admin

# Register your models here.

from .models import RiskName,RiskDetails

admin.site.register(RiskName)

admin.site.register(RiskDetails)
