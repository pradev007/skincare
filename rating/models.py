from django.db import models

# Create your models here.
class RatingModel(models.Model):
    happy_clients = models.CharField(max_length=10)
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    year_exp = models.PositiveIntegerField()
    services = models.PositiveIntegerField()

    def __str__(self):
        return self.happy_clients
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        ordering = ['-rating']