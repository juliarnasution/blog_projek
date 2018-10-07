from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=255)
    body  = models.TextField()
    # date  = models.DateField()
    # image = models.ImageField(upload_to='image')
    date  = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='image')
    # author =  models.ForeignKey(User)

    def __str__(self):
    	return self.title
