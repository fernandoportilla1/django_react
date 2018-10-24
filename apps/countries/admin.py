from django.contrib import admin

from apps.countries.models import Country


# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('is_available',)


admin.site.register(Country, CountryAdmin)
