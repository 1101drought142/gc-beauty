from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import ItemCategories, Item, Certificates, Banners, Tags, Types, Team, Photos, CallbackForm
# Register your models here.

admin.site.register(ItemCategories)
admin.site.register(Certificates)
admin.site.register(Banners)
admin.site.register(Tags)
admin.site.register(Types)
admin.site.register(Team)

class CallbackFormAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', "name", "phone")
admin.site.register(CallbackForm, CallbackFormAdmin)


class ImageAdminInline(TabularInline):
        extra = 1
        model = Photos



@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    inlines = (ImageAdminInline,)

@admin.register(Photos)
class PhotosModelAdmin(admin.ModelAdmin):
    fields = ('src', 'product')