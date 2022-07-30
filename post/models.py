from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Published')

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:post_detail", args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug,
        ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.status = 'Published'
        super(Post, self).save(*args, **kwargs)