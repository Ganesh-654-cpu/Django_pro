# from django.contrib import admin

# # Register your models here.

# from .models import reg,employee
# admin.site.register([reg,employee])

from django.contrib import admin
from .models import reg, employee, person


admin.site.register(reg)
admin.site.register(employee)
admin.site.register(person)

