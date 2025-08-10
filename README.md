# Shivam Chaubey - Personal Portfolio Website

A clean, professional portfolio website inspired by The New York Times design aesthetic, built with Django.

#### Features

- **Clean NYT-inspired Design**: Professional typography using Lora (serif) and Inter (sans-serif) fonts
- **Secret Admin Panel**: Content management system at `/admin` for blogs, projects, and site settings
- **Rich Text Editor**: CKEditor integration for creating blog posts with formatting, images, and links
- **Responsive Design**: Mobile-friendly layout with hamburger navigation
- **Project Showcase**: Featured projects with images, descriptions, and technology tags
- **Blog System**: Full-featured blog with search, pagination, and rich content
- **Resume Download**: Integrated resume management and download functionality


 1. To Start the Container:

   docker run -d -p 8000:8000 -v $(pwd):/app --env-file .env shivams_portfolio gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:8000 --reload

  2. To Stop the Container:

   1 docker stop $(docker ps -a -q)
