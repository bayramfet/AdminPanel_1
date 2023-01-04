from django.contrib import admin

from .models import Product

# admin.site.register(Product)

# ---------------- ProductAdmin --------------------

class ProductAdmin(admin.ModelAdmin):
    # Tablo sutunları:
    list_display = ['id', 'name', 'is_in_stock', 'slug', 'create_date', 'update_date']
    # Kayda gitmek için linkleme:
    list_display_links = ['id', 'name']
    # Tablo üzerinde güncelleyebilme:
    list_editable = ['is_in_stock']
    # Filtreleme (arama değil):
    list_filter = ['is_in_stock', 'create_date', 'update_date']
    # Arama:
    search_fields = ('id', 'name')
    search_help_text = 'Arama işlemlerini buradan yapabilrsiniz.'
    # Default Sıralama:
    ordering = ('-id',)
    # Sayfa başına kayıt sayısı:
    list_per_page = 20
    # Tümünü göster yaparken max kayıt sayısı:
    list_max_show_all = 999
    # Tarihe göre filtreleme başlığı:
    date_hierarchy = 'create_date'
    # Otomatik kaıyıt oluştur:
    prepopulated_fields = {'slug': ['name']}

    

# Call:
admin.site.register(Product, ProductAdmin)