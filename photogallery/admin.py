from django.contrib import admin
from .models import Photo,Category,Location

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('categories',)

admin.site.register(Location)
admin.site.register(Photo,admin_class=ImageAdmin)
admin.site.register(Category)