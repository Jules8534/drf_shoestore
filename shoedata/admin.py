from django.contrib import admin
from shoedata.models import Manufacturer, ShoeType, ShoeColor, Shoe, User

# Register your models here.

admin.site.register(Manufacturer)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Shoe)
#admin.site.register(User)
