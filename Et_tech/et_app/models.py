from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='et_app_user_groups',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='et_app_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username
    
    


class Content(models.Model):
    """Model for website content (pages, blog posts, projects)."""
    CONTENT_TYPE_CHOICES = (
        ('page', 'Page'),
        ('blog_post', 'Blog Post'),
        ('project', 'Project'),
    )
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    hero_image = models.ForeignKey(to='Image', on_delete=models.SET_NULL, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

class Service(models.Model):
    """Model for website services."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)

class Project(models.Model):
    """Model for website projects."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey(to='Image', on_delete=models.SET_NULL, null=True)
    outcomes = models.TextField()
    content = models.ManyToManyField(to=Content, blank=True)  # Link related content

class TeamMember(models.Model):
    """Model for website team members."""
    name = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ForeignKey(to='Image', on_delete=models.SET_NULL, null=True)

class Career(models.Model):
    """Model for website careers."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    application_form_link = models.URLField()

class Image(models.Model):
    """Model for website images."""
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255)

class Category(models.Model):
    """Model for website service categories."""
    name = models.CharField(max_length=255)