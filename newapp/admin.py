from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Location)
admin.site.register(Payment)
admin.site.register(Poll)
admin.site.register(Choice)