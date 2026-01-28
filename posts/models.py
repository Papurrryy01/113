from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256, help_text="A brief description of the status")

    class Meta:
        verbose_name = "status"
        verbose_name_plural = "statuses"

    def __str__(self):
        return self.name





class Post(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
