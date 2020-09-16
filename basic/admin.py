from django.contrib import admin

from .models import Index

# Register your models here
admin.site.site_header = "Admin"


admin.site.register(Index)






