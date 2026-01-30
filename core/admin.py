from django.contrib import admin
from .models import Event, Gallery, Contact, About, SiteSettings

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'price_min', 'price_max', 'is_featured', 'is_active', 'created_at']
    list_filter = ['is_featured', 'is_active', 'date', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured', 'is_active']
    date_hierarchy = 'date'
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'icon', 'image')
        }),
        ('Nội dung', {
            'fields': ('description',)
        }),
        ('Thời gian và giá', {
            'fields': ('date', 'price_min', 'price_max')
        }),
        ('Hiển thị', {
            'fields': ('is_featured', 'is_active')
        }),
    )

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover; border-radius: 5px;"/>'
        return '-'
    image_preview.short_description = 'Hình ảnh'
    image_preview.allow_tags = True

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']
    fieldsets = (
        ('Thông tin liên hệ', {
            'fields': ('name', 'email', 'phone', 'created_at')
        }),
        ('Nội dung', {
            'fields': ('message',)
        }),
        ('Trạng thái', {
            'fields': ('is_read',)
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'content']
    list_editable = ['order', 'is_active']
    fieldsets = (
        ('Thông tin', {
            'fields': ('title', 'image')
        }),
        ('Nội dung', {
            'fields': ('content',)
        }),
        ('Hiển thị', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'phone', 'email']
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('site_name', 'site_title', 'site_description')
        }),
        ('Logo & Favicon', {
            'fields': ('logo', 'favicon')
        }),
        ('Liên hệ', {
            'fields': ('phone', 'email', 'address', 'zalo_phone')
        }),
        ('Mạng xã hội', {
            'fields': ('facebook_url', 'youtube_url', 'instagram_url')
        }),
        ('SEO & Marketing', {
            'fields': ('keywords', 'og_image', 'google_analytics', 'google_site_verification', 'facebook_pixel'),
            'description': 'Cấu hình SEO và công cụ marketing'
        }),
    )
    
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
