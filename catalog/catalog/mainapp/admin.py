from django.contrib import admin

from mainapp.models import Provider, Measure, Catalog


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class MeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'add_time', 'measure', 'provider')
    list_display_links = ('id', 'name', 'price', 'add_time', 'measure', 'provider')


admin.site.register(Provider, ProviderAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(Catalog, CatalogAdmin)
