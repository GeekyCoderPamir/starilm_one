from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)
    detail_link = models.URLField(blank=True)

    def _str__(self):
        return self.title
