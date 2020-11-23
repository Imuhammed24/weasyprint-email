from django.db import models

# Create your models here.
class Email(models.Model):
    slug = models.CharField(max_length=120)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
