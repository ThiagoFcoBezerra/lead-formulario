from django.contrib import admin
from form_lead.models import Cupon

class ListaCupon(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cupon')
    list_display_links = ('id','nome')
    search_fields = ('nome','cupon')

admin.site.register(Cupon, ListaCupon)
