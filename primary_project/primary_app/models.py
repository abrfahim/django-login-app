from django.db import models
from django.urls import reverse
# Create your models here.

class Musician(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    instrument = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_absolute_url(self):
        return reverse('class_app:musician_details', kwargs={'pk':self.pk})
            
class Album(models.Model):
    # id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Musician, on_delete= models.CASCADE, related_name='album_list')
    name =  models.CharField(max_length = 100)
    release_date = models.DateField()
    
    rating = (
        (1,'Very Bad'),
        (2,'Bad'),
        (3,'Average'),
        (4,'Good'),
        (5,'Very Good'),
    )
    
    num_stars = models.IntegerField(choices=rating)
    
    def __str__(self):
        return self.name + ' Ratings:' + str(self.num_stars)