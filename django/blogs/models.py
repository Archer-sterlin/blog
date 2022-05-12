from django.conf import settings
from django.db import models
from django.urls import reverse
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media',default='default.png', blank=True)
    status = models.CharField(max_length=10, choices=options, default='published')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:80] + '...'
    
    def get_absolute_url(self):
        return reverse('blogs:detail', args=[str(self.id)])