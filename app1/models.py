from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 100)
    headquarters = models.CharField(max_length = 100)
    industry = models.CharField(max_length = 100, null = True)
    founding_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100, default = 'not available')
    company = models.ForeignKey(Company, on_delete = models.CASCADE, related_name = 'employees')

    def __str__(self):
        return self.name
    