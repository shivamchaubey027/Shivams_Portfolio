from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class BlogPost(models.Model):
    """Model for blog posts with rich text content"""
    title = models.CharField(max_length=200, help_text="The title of your blog post")
    slug = models.SlugField(max_length=200, unique=True, blank=True, 
                           help_text="URL-friendly version of the title (auto-generated)")
    excerpt = models.TextField(max_length=300, 
                              help_text="Brief description shown on blog listing page")
    content = RichTextUploadingField(help_text="Full blog post content with rich text editor")
    is_featured = models.BooleanField(default=False, 
                                     help_text="Show on homepage featured section")
    is_published = models.BooleanField(default=True, 
                                      help_text="Make this post visible to visitors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now, 
                                       help_text="When this post should be published")

    class Meta:
        ordering = ['-published_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200, help_text="Project name")
    description = models.TextField(help_text="Brief description of the project")
    detailed_description = RichTextUploadingField(blank=True, 
                                                 help_text="Detailed project description (optional)")
    image = models.ImageField(upload_to='project_images/', blank=True, null=True,
                             help_text="Project screenshot or image")
    live_url = models.URLField(blank=True, help_text="Live demo URL (optional)")
    github_url = models.URLField(blank=True, help_text="GitHub repository URL (optional)")
    tech_stack = models.CharField(max_length=300, 
                                 help_text="Technologies used (comma-separated)")
    is_featured = models.BooleanField(default=False, 
                                     help_text="Show on homepage featured section")
    is_active = models.BooleanField(default=True, 
                                   help_text="Display this project on the website")
    order = models.PositiveIntegerField(default=0, 
                                       help_text="Display order (lower numbers first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    @property
    def tech_stack_list(self):
        """Convert comma-separated tech stack to list"""
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]


class Resume(models.Model):
    """Model for resume file management"""
    title = models.CharField(max_length=100, default="My Resume")
    file = models.FileField(upload_to='resumes/', 
                           help_text="Upload your resume as PDF")
    is_active = models.BooleanField(default=True, 
                                   help_text="Make this resume available for download")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return f"{self.title} - {self.uploaded_at.strftime('%Y-%m-%d')}"


class SiteSettings(models.Model):
    """Model for site-wide settings and personal information"""
    site_title = models.CharField(max_length=100, default="My Portfolio")
    tagline = models.CharField(max_length=200, 
                              default="Software Developer & Creative Technologist")
    bio_short = models.TextField(max_length=500, 
                                help_text="Brief bio for homepage hero section")
    bio_long = RichTextUploadingField(help_text="Detailed bio for about page")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True,
                                     help_text="Professional headshot")
    
    # Contact Information
    email = models.EmailField(help_text="Professional email address")
    github_url = models.URLField(blank=True, help_text="GitHub profile URL")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter/X profile URL")
    
    # SEO
    meta_description = models.TextField(max_length=160, blank=True,
                                       help_text="Site description for search engines")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return f"Site Settings - {self.site_title}"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError("Only one SiteSettings instance is allowed")
        super().save(*args, **kwargs)
