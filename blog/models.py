from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author_name = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    summary = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
