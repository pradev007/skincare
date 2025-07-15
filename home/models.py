from datetime import timezone
from django.db import models
from account.models import CustomUser
# Create your models here.
class HeadingModel(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Heading'
        verbose_name_plural = 'Headings'
        ordering = ['-created_at']
