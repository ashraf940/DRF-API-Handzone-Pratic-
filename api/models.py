from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    about= models.TextField()
    type = models.CharField(max_length=200, choices=
                            [("IT","IT"),
                            ("Non IT","Non IT"),
                            ("Mobile Phones","Mobile Phones")])
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name + '--' + self.location

    
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    position = models.CharField(max_length=50, choices=
                            [("Manager","Manager"),
                            ("Developer","Developer"),
                            ("Designer","Designer"),
                            ("Tester","Tester")])
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    