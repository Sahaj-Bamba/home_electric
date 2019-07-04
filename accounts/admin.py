from django.contrib import admin
from . import models

admin.site.register(models.consumption)
admin.site.register(models.my_users)
admin.site.register(models.payment)
admin.site.register(models.user_details)
admin.site.register(models.bill)

# Register your models here.
