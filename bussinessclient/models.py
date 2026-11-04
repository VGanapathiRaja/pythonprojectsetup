from django.db import models

# Create your models here.
class students(models.Model):
    sname = models.TextField(max_length=100)
    semail= models.EmailField(max_length=100)
    smobile = models.BigIntegerField()
    sage = models.IntegerField()

    def __str__(self):
        return self.name


# class Bid(models.Model):
#     item = models.ForeignKey(Listing, on_delete=models.CASCADE)
#     price = models.FloatField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)