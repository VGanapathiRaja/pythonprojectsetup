from django.db import models

# Create your models here.
class students(models.Model):
    sname = models.TextField(max_length=100)
    semail= models.EmailField(max_length=100,null=True, blank=True)
    smobile = models.BigIntegerField()
    sage = models.IntegerField()

    def __str__(self):
        return self.name


class Signin(models.Model):
      susername = models.TextField(max_length=100)
      semail = models.EmailField(max_length=100)
      spass = models.TextField(max_length=6)
      scpass = models.TextField(max_length=6)

      def __str__(self):
           return self.name
