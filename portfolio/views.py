from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost, Project, Resume, SiteSettings


def get_site_settings():
    """Get or create site settings"""
    settings, created = SiteSettings.objects.get_or_create(
        pk=1,
        defaults={
            'site_title': 'Shivam Chaubey',
            'tagline': 'Engineering Student & Backend Developer',
            'bio_short': 'Self-driven engineering student with hands-on experience in backend development, data science, and full-stack prototyping. Skilled in Python, Java, and JavaScript.',
            'bio_long': 'I am passionate about building ML-powered tools with clean UI, strong logic, and real-world impact. Currently pursuing B.E. in CSE (AI & ML) at Mumbai University.',
            'email': 'shivamchaubey027@gmail.com',
            'github_url': 'https://github.com/shivamchaubey',
            'linkedin_url': 'https://linkedin.com/in/shivamchaubey',
        }
    )
    return settings


def index(request):
    """Homepage with featured content"""
    site_settings = get_site_settings()
    featured_projects = Project.objects.filter(is_active=True, is_featured=True)[:3]
    featured_blogs = BlogPost.objects.filter(is_published=True, is_featured=True)[:3]
    latest_blogs = BlogPost.objects.filter(is_published=True)[:3]
    
    context = {
        'site_settings': site_settings,
        'featured_projects': featured_projects,
        'featured_blogs': featured_blogs,
        'latest_blogs': latest_blogs,
    }
    return render(request, 'portfolio/index.html', context)


def blog_list(request):
    """Blog listing page with pagination"""
    blog_posts = BlogPost.objects.filter(is_published=True)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        blog_posts = blog_posts.filter(
            Q(title__icontains=search_query) |
            Q(excerpt__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(blog_posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'site_settings': get_site_settings(),
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'portfolio/blog_list.html', context)


def blog_detail(request, slug):
    """Individual blog post page"""
    blog_post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    # Get related posts (same as current post's tags or recent posts)
    related_posts = BlogPost.objects.filter(
        is_published=True
    ).exclude(id=blog_post.id)[:3]
    
    context = {
        'site_settings': get_site_settings(),
        'blog_post': blog_post,
        'related_posts': related_posts,
    }
    return render(request, 'portfolio/blog_detail.html', context)


def projects(request):
    """Projects showcase page"""
    all_projects = Project.objects.filter(is_active=True)
    
    # Filter by technology if provided
    tech_filter = request.GET.get('tech')
    if tech_filter:
        all_projects = all_projects.filter(tech_stack__icontains=tech_filter)
    
    # Get all unique technologies for filter
    all_tech = set()
    for project in Project.objects.filter(is_active=True):
        all_tech.update(project.tech_stack_list)
    all_tech = sorted(list(all_tech))
    
    context = {
        'site_settings': get_site_settings(),
        'projects': all_projects,
        'all_tech': all_tech,
        'current_tech': tech_filter,
    }
    return render(request, 'portfolio/projects.html', context)


def about(request):
    """About page"""
    site_settings = get_site_settings()
    
    context = {
        'site_settings': site_settings,
    }
    return render(request, 'portfolio/about.html', context)


def contact(request):
    """Contact page"""
    site_settings = get_site_settings()
    
    # Handle contact form submission
    success_message = None
    if request.method == 'POST':
        # In a real application, you would handle form submission here
        # For now, we'll just show a success message
        success_message = "Thank you for your message! I'll get back to you soon."
    
    context = {
        'site_settings': site_settings,
        'success_message': success_message,
    }
    return render(request, 'portfolio/contact.html', context)


def download_resume(request):
    """Handle resume download"""
    try:
        resume = Resume.objects.filter(is_active=True).first()
        if not resume or not resume.file:
            raise Http404("Resume not found")
        
        response = HttpResponse(resume.file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume.title}.pdf"'
        return response
    except Resume.DoesNotExist:
        raise Http404("Resume not found")
