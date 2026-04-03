from django.db import models
class Review(models.Model):
    product=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    rating=models.IntegerField()
    comment=models.TextField()
    
    def __str__(self):
        return self.product
    
# Create your models here.
