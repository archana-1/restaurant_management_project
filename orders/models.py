from django.db import models
from account.models import Customer, Restaurant
# Create your models here.
class OrderStatus(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name
    


    
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.CharField(max_length=50)


    def __str__(self):
        return self.code
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL,null = True )
    coupon_code = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True)
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.customer.name+""+str(self.total_price)
    

