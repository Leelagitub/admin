from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    ceo = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cardapp:detail" ,kwargs={"pk":self.pk})

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    miliege = models.IntegerField()
    cc = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=200)
    year = models.IntegerField()
    company = models.ForeignKey(Company,related_name='companies',on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name