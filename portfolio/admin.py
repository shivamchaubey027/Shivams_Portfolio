from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import BlogPost, Project, Resume, SiteSettings


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Admin interface for blog posts"""
    list_display = ['title', 'is_published', 'is_featured', 'published_at', 'view_on_site_link']
    list_filter = ['is_published', 'is_featured', 'created_at', 'published_at']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Publishing', {
            'fields': ('is_published', 'is_featured', 'published_at')
        }),
    )
    
    def view_on_site_link(self, obj):
        if obj.is_published:
            url = obj.get_absolute_url()
            return format_html('<a href="{}" target="_blank">View</a>', url)
        return "Not published"
    view_on_site_link.short_description = "View on site"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for projects"""
    list_display = ['title', 'is_active', 'is_featured', 'order', 'tech_stack_preview', 'links']
    list_filter = ['is_active', 'is_featured', 'created_at']
    search_fields = ['title', 'description', 'tech_stack']
    list_editable = ['order', 'is_featured', 'is_active']
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'detailed_description', 'image')
        }),
        ('Links', {
            'fields': ('live_url', 'github_url')
        }),
        ('Technical Details', {
            'fields': ('tech_stack',)
        }),
        ('Display Settings', {
            'fields': ('is_active', 'is_featured', 'order')
        }),
    )
    
    def tech_stack_preview(self, obj):
        tech_list = obj.tech_stack_list[:3]  # Show first 3 technologies
        preview = ', '.join(tech_list)
        if len(obj.tech_stack_list) > 3:
            preview += f" (+ {len(obj.tech_stack_list) - 3} more)"
        return preview
    tech_stack_preview.short_description = "Technologies"
    
    def links(self, obj):
        links = []
        if obj.live_url:
            links.append(f'<a href="{obj.live_url}" target="_blank">Live Site</a>')
        if obj.github_url:
            links.append(f'<a href="{obj.github_url}" target="_blank">GitHub</a>')
        return mark_safe(' | '.join(links)) if links else "No links"
    links.short_description = "Links"


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """Admin interface for resume management"""
    list_display = ['title', 'is_active', 'uploaded_at', 'download_link']
    list_filter = ['is_active', 'uploaded_at']
    
    def download_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">Download</a>', obj.file.url)
        return "No file"
    download_link.short_description = "Download"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Admin interface for site settings"""
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_title', 'tagline', 'bio_short', 'bio_long', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'github_url', 'linkedin_url', 'twitter_url')
        }),
        ('SEO', {
            'fields': ('meta_description',)
        }),
    )
    
    def has_add_permission(self, request):
        # Prevent adding multiple instances
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the settings
        return False


# Customize the admin site
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to your Portfolio Administration"
