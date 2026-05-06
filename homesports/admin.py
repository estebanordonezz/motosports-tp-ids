from django.contrib import admin
from .models import Moto, Categoria

admin.site.register(Moto)

admin.site.register(Categoria)
class MotoAdmin(admin.ModelAdmin):
    list_display = ("categoria", "marca", "modelo", "año")
    search_fields = ("marca", "modelo")
    list_filter = ("categoria", "año")