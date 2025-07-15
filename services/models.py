from django.db import models

# Create your models here.
class Services(models.Model):
    treatments = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)
    price = models.IntegerField()
    descriptions = models.CharField(max_length=255)
    included = models.JSONField()
    is_popular = models.BooleanField(default=False)
    image = models.ImageField(upload_to='services/', blank=True,null=True)

    def __str__(self):
        return self.treatments
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-price']
