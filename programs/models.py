from django.db import models

# Create your models here.
class ProgramModel(models.Model):
    program_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='program/', null= True, blank=True)

    def __str__(self):
        return self.program_name
    
    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'
        ordering = ['-program_name']