from django.db import models

# Create your models here.

from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# AVAILABLE = (
#      (0,"Available"),
#      (1,"Not Available")
# )

class Listings(models.Model):
    address = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    content = models.TextField()
    pictures = models.ImageField(upload_to='images/',default='default.jpg')
    created_on = models.DateTimeField(auto_now_add=True)
    # available = models.IntegerField(choices=AVAILABLE, default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.address