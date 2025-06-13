from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('projects/', views.projects, name='projects'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('download-resume/', views.download_resume, name='download_resume'),
    path('create-my-admin-user-now-12345/', views.create_superuser_view, name='create_superuser'),

]
