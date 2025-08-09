from django.contrib import admin
from django.utils.html import format_html
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail_preview", "released_at", "is_public")
    list_editable = ("is_public",)
    search_fields = ("title", "released_at")

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="height: 60px; border-radius: 4px;" />', obj.thumbnail.url)
        return "—"

    thumbnail_preview.short_description = "Thumbnail"


admin.site.register(Post, PostAdmin)