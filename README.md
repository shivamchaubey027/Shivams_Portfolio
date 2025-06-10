# Shivam Chaubey - Personal Portfolio Website

A clean, professional portfolio website inspired by The New York Times design aesthetic, built with Django.

## Features

- **Clean NYT-inspired Design**: Professional typography using Lora (serif) and Inter (sans-serif) fonts
- **Secret Admin Panel**: Content management system at `/admin` for blogs, projects, and site settings
- **Rich Text Editor**: CKEditor integration for creating blog posts with formatting, images, and links
- **Responsive Design**: Mobile-friendly layout with hamburger navigation
- **Project Showcase**: Featured projects with images, descriptions, and technology tags
- **Blog System**: Full-featured blog with search, pagination, and rich content
- **Resume Download**: Integrated resume management and download functionality

## Tech Stack

- **Backend**: Django 5.2.3, Python
- **Database**: SQLite (development), PostgreSQL (production)
- **Rich Text**: django-ckeditor
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Fonts**: Google Fonts (Lora, Inter, Source Code Pro)

## Local Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd portfolio-website
   ```

2. **Install dependencies**
   ```bash
   pip install django django-ckeditor pillow
   ```

3. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser account**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

5. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access your website**
   - Main website: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Content Management

### Admin Panel Access
- URL: `/admin`
- Default credentials (if using the provided setup):
  - Username: admin
  - Password: admin123

### Managing Content

1. **Site Settings**: Update your personal information, bio, contact details, and social links
2. **Projects**: Add your portfolio projects with images, descriptions, and technology stacks
3. **Blog Posts**: Create blog articles with the rich text editor
4. **Resume**: Upload your resume PDF for download functionality

### Adding Projects
In the admin panel, go to Portfolio → Projects:
- **Title**: Project name
- **Description**: Brief project overview
- **Detailed Description**: Full project details (supports rich text)
- **Image**: Project screenshot or logo
- **Live URL**: Link to live demo
- **GitHub URL**: Repository link
- **Tech Stack**: Comma-separated list of technologies
- **Is Featured**: Check to display on homepage
- **Order**: Number for display ordering (lower = first)

### Writing Blog Posts
In the admin panel, go to Portfolio → Blog Posts:
- **Title**: Post title (slug auto-generated)
- **Excerpt**: Brief description for listings
- **Content**: Full post content with rich text editor
- **Is Featured**: Check to display on homepage
- **Published At**: When to publish the post

## Free Deployment Options

### 1. PythonAnywhere (Recommended)
- **Free Tier**: 1 web app, 512MB storage, good for portfolio sites
- **Steps**:
  1. Create account at pythonanywhere.com
  2. Upload your code via Git or file manager
  3. Set up web app in dashboard (Django, Python 3.8+)
  4. Configure static files and database
  5. Add your domain in settings

### 2. Railway
- **Free Tier**: $5 credit monthly, auto-sleeps after inactivity
- **Steps**:
  1. Connect GitHub repository to Railway
  2. Deploy with automatic Django detection
  3. Add PostgreSQL database
  4. Set environment variables

### 3. Render
- **Free Tier**: 750 hours/month, auto-sleeps after 15 minutes
- **Steps**:
  1. Connect GitHub repository
  2. Select "Web Service"
  3. Use build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
  4. Use start command: `python manage.py runserver 0.0.0.0:$PORT`

### 4. Heroku (Limited Free Tier)
- **Note**: Heroku discontinued free tier but offers student credits
- **Steps**: Similar to Railway, requires buildpack configuration

## Production Configuration

### Environment Variables
For production deployment, set these environment variables:

```bash
DEBUG=False
DJANGO_SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url (for PostgreSQL)
ALLOWED_HOSTS=your-domain.com
```

### Database Migration
For PostgreSQL in production:

1. Install psycopg2: `pip install psycopg2-binary`
2. Update settings.py database configuration
3. Run migrations: `python manage.py migrate`

### Static Files
For production with cloud storage:

1. Install whitenoise: `pip install whitenoise`
2. Add to MIDDLEWARE in settings.py
3. Configure STATIC_ROOT and STATICFILES_STORAGE

## Project Structure

```
portfolio_site/
├── manage.py
├── portfolio_site/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/
│   ├── models.py          # Data models (BlogPost, Project, etc.)
│   ├── views.py           # View functions
│   ├── admin.py           # Admin panel configuration
│   ├── urls.py            # URL routing
│   └── migrations/
├── templates/
│   ├── base.html          # Base template
│   └── portfolio/         # Page templates
├── static/
│   ├── css/style.css      # Main stylesheet
│   └── js/main.js         # JavaScript functionality
└── media/                 # Uploaded files (images, resume)
```

## Customization

### Changing Colors
Edit `static/css/style.css` to modify the color scheme. Key color variables are used throughout for consistency.

### Adding New Pages
1. Create view function in `portfolio/views.py`
2. Add URL pattern in `portfolio/urls.py`
3. Create template in `templates/portfolio/`

### Modifying Navigation
Update the navigation in `templates/base.html` to add or remove menu items.

## Security Notes

- Change default admin credentials before deployment
- Use strong SECRET_KEY in production
- Set DEBUG=False in production
- Configure ALLOWED_HOSTS properly
- Keep dependencies updated

## Support

For issues or questions about the portfolio setup, refer to Django documentation or create an issue in the repository.

## License

This project is open source and available under the MIT License.