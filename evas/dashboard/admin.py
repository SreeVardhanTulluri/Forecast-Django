from django.contrib import admin

# Register your models here.
from .models import *

class inventoryAdmin(admin.ModelAdmin):
    list_display = ("clientno", "gloryid")

admin.site.register(Inventory,inventoryAdmin)
admin.site.register(InventoryDtl,inventoryAdmin)
admin.site.register(Mediamap)