from django.db import models

class Animal(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return str(self.tag)

class Capture(models.Model):
    animal = models.ForeignKey(Animal, related_name='captures',on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='images/')
    newCap = models.BooleanField(default=False)

    def __str__(self):
        return str(self.animal)+str(self.pk)
