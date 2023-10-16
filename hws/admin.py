from django.contrib import admin
from hws.models import User, Product, Order

# Register your models here.

class OrderInline(admin.TabularInline):
    model = Order.products.through

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'add_date']
    ordering = ['-quantity']
    search_fields = ['name']
    list_per_page = 5
    
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    ordering = ['name']
    search_fields = ['name']
    list_per_page = 5
    readonly_fields = ['email', 'phone']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price']
    ordering = ['-total_price']
    search_fields = ['custumer']
    list_per_page = 5
    readonly_fields = ['total_price']
    inlines = [OrderInline]
    exclude = ['products']

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)