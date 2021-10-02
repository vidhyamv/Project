from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__ (self):
        return self.name
class space(models.Model):
    image=models.ImageField(upload_to='photo')
    date=models.DateField()
    tit=models.CharField(max_length=250)
    disc=models.TextField()



