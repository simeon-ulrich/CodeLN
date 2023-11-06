
from django.contrib import admin

from actions.action import Action
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username",
        "last_name",
        "first_name",
        "email","date_update", "date_joined", "status")
    list_display_links = ["username", "email"]
    search_fields = ("username", "email","date_joined")
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("status",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ( "date_joined","status")}),
    )

    list_filter = UserAdmin.list_filter + ("status","date_joined")
    
    actions = ["activate", "deactivate"]
    
    def deactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "Désactivation(s) effectué(s)")

    deactivate.short_description = "Désactiver les utilisateurs selectionnés"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Activation(s) effectué(s)")

    activate.short_description = "Activer les utilisateurs selectionnés"



@admin.register(models.Badge)
class BadgeAdmin(Action):
    list_display = ("badge_type", "user", "date_add",)
    list_display_links = ["user", "badge_type"]
    search_fields = ("user", "badge_type","date_add")

@admin.register(models.Model3d)
class Model3dAdmin(Action):
    list_display = ("description", "user", "views" , "image_linkview")
    list_display_links = ["description", "user", "image_linkview"]
    search_fields = ("user", "description")
    
    
    def image_linkview(self, obj):
        if obj.image_link:
            return mark_safe(
                f'<img src="{obj.image_link.url}" style="height:60px; width:60px">'
            )
        else:
            return "Aucun fichier"

    image_linkview.short_description = "Image 3d"