from django.db import models




class Color(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name
    
    



# Create your models here.
class People(models.Model):
    color = models.ForeignKey(Color, null= True,blank=True,on_delete=models.CASCADE, related_name='color')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    