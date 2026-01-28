from django.db import models
from django.utils import timezone
from datetime import date


class Songs(models.Model):
    TUNETYPE = (
        ('N/A', 'N/A'),
        ('Jig', 'Jig'),
        ('Reel', 'Reel'),
        ('Polka', 'Polka'),
        ('Listening Tune', 'Listening_Tune')
    )

    title = models.CharField(max_length=50, null=True, blank=True, unique=True)
    description = models.TextField(blank=True)
    tune_type = models.CharField(max_length=25, choices=TUNETYPE)
    file = models.FileField(upload_to="songs/")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.title)

    def delete(self):
        self.file.delete()
        super().delete()

class Testimonials(models.Model):
    heading = models.CharField(max_length=250)
    content_text = models.TextField(blank=True)
    image_file= models.ImageField(upload_to="images/")   
    article_created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering =['-article_created_at']

    def __str__(self):
        return str(self.heading)
    
    def delete(self):
        self.image_file.delete()
        super().delete()

class Events(models.Model):
    heading = models.CharField(max_length=250)
    content_text = models.TextField(blank=True)
    image_file= models.ImageField(upload_to="images/")
    expire = models.DateTimeField(default=timezone.now)
    article_created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering =['-article_created_at']

    def __str__(self):
        return str(self.heading)
    
    def delete(self):
        self.image_file.delete()
        super().delete()

class Links(models.Model):
    link_name = models.URLField()
    description = models.TextField(blank=True)

    class Meta:
        ordering=['link_name']

class Gallery(models.Model):
    heading = models.CharField(max_length=250)
    content_text = models.TextField(blank=True)
    image_file= models.ImageField(upload_to="images/gallery")
    article_created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering =['article_created_at']

    def __str__(self):
        return str(self.heading)
    
    def delete(self):
        self.image_file.delete()
        super().delete()
