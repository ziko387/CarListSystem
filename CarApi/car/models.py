from django.db import models

# Create your models here.
class product (models.Model):
    Brand = models.CharField(max_length=1000, unique= True)
    Image = models.ImageField(upload_to='images/')
    name= models.CharField(max_length=1030)
    phonenumber= models.CharField(max_length=10)
    price = models.IntegerField()  

    def __str__(self):
        return self.Brand 
class Order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at= models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)


    @property
    def Total(self):
        return self.product.price *self.quantity



