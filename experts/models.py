from django.db import models

# Create your models here.
class ExpertModel(models.Model):
    name = models.CharField(max_length=255, blank= False, null= False )
    profession = models.CharField(max_length= 255)
    description = models.CharField(max_length= 255)
    experience = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    specialties = models.JSONField()
    certifications = models.JSONField()

    def __str__(self):
        return self.name