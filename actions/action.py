from django.contrib import admin


class Action(admin.ModelAdmin):

    date_hierarchy = "date_add"
    ordering = ("-date_add",)
    list_filter = ("status",)
    list_per_page = 50

    actions = ["activate", "deactivate"]

    def deactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "Désactivation(s) effectué(s)")

    deactivate.short_description = "Désactiver les elements selectionnés"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Activation(s) effectué(s)")

    activate.short_description = "Activer les elements selectionnés"

    # def log_addition(self, *args):
    #     return

    # def log_change(self, *args):
    #     return

    # def log_deletion(self, *args):
    #     return
