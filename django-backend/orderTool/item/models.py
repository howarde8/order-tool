# from django.db import models
# from django.contrib.auth.models import User
# # # Create your models here.

# class Product(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     price = models.FloatField(max_length=30, null=False)
#     upload_time = models.DateTimeField(max_length=30, auto_now=True)
#     name = models.CharField(max_length=30, null=False)
#     category = models.CharField(max_length=30, null=False)
#     quantity = models.IntegerField(null=False)
#     description = models.CharField(max_length=30, null=False)
#     class Meta:
#         app_label = "item"
#         db_table = "product"

# class Order(models.Model):
#     upload_time = models.DateTimeField(max_length=30, auto_now=True)
#     status = models.CharField(max_length=30, null=False)
#     total_price = models.FloatField(max_length=30, null=False)
#     description = models.CharField(max_length=30, null=False)
#     seller_username = models.ForeignKey(User, on_delete=models.CASCADE)
#     buyer_username = models.ForeignKey(User, on_delete=models.CASCADE)
#     class Meta:
#         app_label = "item"
#         db_table = "order"
