from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):
#    This PostObjects is actually a filter or a manager for posts that has status published
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status= 'published')

# Options are for status of posts
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )


    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    # Slug is actually for indentifying a paticular on a website
    slug = models.SlugField(max_length=250, unique_for_date='published') 
    published = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')

    # These are the managers 
    objects = models.Manager() # default manager of filter not applied
    Postobjects = PostObjects() # custom manager if filter is applied

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

