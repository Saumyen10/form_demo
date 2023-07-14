from django.db import models

# Create your models here.
class Zone (models.Model):
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Division (models.Model):
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
class SubDivision (models.Model):
    division = models.ForeignKey(Division,on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
    
