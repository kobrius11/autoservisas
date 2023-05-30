from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.CarModel)
admin.site.register(models.Car)
admin.site.register(models.Order)
admin.site.register(models.Service)
admin.site.register(models.OrderField)