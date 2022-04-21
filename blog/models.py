from turtle import title
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10000)

    def __str__(self):
        return self.name

class Post(models.Model):
    categories = models.ManyToManyField(Category, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='date', null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blog images/', null=True)
    # likes = models.ManyToManyField(User, related_name='blog_post', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f'{self.title} by {self.author.username} ({self.categories.name})'

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])
    
    def get_days(self):
        current = timezone.now()
        delta = current - self.date
        if delta.days <= 1:
            return f'{delta.days} day ago'
        else:
            return f'{delta.days} days ago'


# Comment on posts
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('blog:post_list')


