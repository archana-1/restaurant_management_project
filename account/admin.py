from django.contrib import admin
from .models import Restaurant, CustomUser,Customer,CustomUserManager, MenuItem
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(CustomUser)
admin.site.register(MenuItem)
admin.site.register(Customer)