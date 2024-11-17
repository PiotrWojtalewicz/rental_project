from django.contrib import admin
from .models import Car, Rental, UserProfile, Payment

admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(UserProfile)
admin.site.register(Payment)
# Register your models here.
