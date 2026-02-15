 
# Register your models here.
from django.contrib import admin
from .models import Salon, Service, Employee

admin.site.register(Salon)
admin.site.register(Service)
admin.site.register(Employee)
