from django.db import models

# Create your models here.
class testapp(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=12345.67)
    desc2 = models.TextField(default='filler text')
    Does_Richard_like_lolis = models.BooleanField(default=True)
