from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'preparation_time', 'category')
    list_editable = ('category')
    list_filter = ('category')
    list_display_links = ('name')
    search_fields = ('name', 'description')

    inlines = [
        ProductImageInline
    ]

    def get_image(self, obj):
        images = ProductImage.objects.filter(product=obj)
        if images:
            product_image = images[0]
            return mark_safe(f"<img src='{product_image.image.url}' style='width: 150px;'>")
        else:
            return "-"

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image')


admin.site.site_header = "BurgerHouse"
admin.site.site_title = "BurgerHouse"
admin.site.index_title = "Admin"
admin.site.login_template = "admin/login.html"

admin.site.register([Category, Product, ProductImage, Additional, Comment])