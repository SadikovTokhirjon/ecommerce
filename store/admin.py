
from django.contrib import admin

from store.models import Category, Product,Order,Customer

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)


