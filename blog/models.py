from django.db import models
from django.utils.text import slugify

# Create your models here.
class Gameblog(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    email = models.EmailField()
    contact_no = models.CharField(max_length=10)
 
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    date = models.DateField()
    image = models.FileField(upload_to='images')
    slug = models.SlugField(default='',null=False,db_index=True,editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super().save(*args, **kwargs)