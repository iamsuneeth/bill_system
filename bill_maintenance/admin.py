from django.contrib import admin
from .models import Product, Bill, BillItem
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class BillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bill, BillAdmin)

class BillItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(BillItem, BillItemAdmin)