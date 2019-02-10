# Register your models here.
from django.contrib import admin
from .models import S_Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    class Meta:
        model = S_Product

admin.site.register(S_Product, ProductAdmin)