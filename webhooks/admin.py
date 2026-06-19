from django.contrib import admin

from .models import Company, Webhook, WebhookEvent


class WebhookEventInline(admin.TabularInline):
    model = WebhookEvent
    extra = 0


@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "company", "target_url", "is_active", "mask_user_agent")
    list_filter = ("is_active", "mask_user_agent")
    search_fields = ("name", "target_url", "company__name")
    inlines = [WebhookEventInline]


admin.site.register(Company)
