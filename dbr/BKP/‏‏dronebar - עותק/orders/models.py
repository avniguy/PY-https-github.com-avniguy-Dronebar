from django.db import models
from shops.models import Menu, MenuItem , Shop #

# Create your models here.
# class OrderStatus(models.Model):
#     name = models.CharField(max_length=12)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name
#

class Order(models.Model):

    OrderStatus = (
        ('New',1),
        ('Pending',2),
        ('Processing',3),
        ('Shipped',4),
        ('Delievered',5),
        ('Closed',6),
        ('Canceled',7),
    )


    customer = models.IntegerField()
    order_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 10, choices = OrderStatus, default = 1)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)
    total_weight = models.FloatField(default=0)
    # items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return "Order number:" + order_id + " , Total: " + total_price

    # def get_absolute_url(self):
    #     return reverse("orders:order_detail",kwargs={"id":self.order_id})


class OrderRow(models.Model):
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    item = models.ForeignKey(MenuItem,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    row_price = models.FloatField(default=0)
    row_weight = models.FloatField(default=0)

    def __str__(self):
        return "Order number:" + self.order.id

    # def get_absolute_url(self):
    #     return reverse("orders:order_detail",kwargs={"id":self.order_id})
