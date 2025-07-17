from django.db import models
from django.utils.text import slugify
from django.core.validators import EmailValidator

# Create your models here.
class Gameblog(models.Model):
    name = models.CharField(max_length=30,blank=False)
    city = models.CharField(max_length=10,blank=False)
    email = models.EmailField(max_length=200,validators=[EmailValidator],blank=False)
    contact_no = models.CharField(max_length=10,blank=False)
 
class GamePurchase(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True ,blank=False)
    contact = models.CharField(max_length=10,default=0)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    games_purchased = models.TextField(null=True)

    
class BlogPost(models.Model):
    title = models.CharField(max_length=50,blank=False)
    summary = models.TextField(blank=False)
    date = models.DateField()
    image = models.FileField(upload_to='images')
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    slug = models.SlugField(default='',null=False,db_index=True,editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super().save(*args, **kwargs)

class TempCart(models.Model):
    game = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
