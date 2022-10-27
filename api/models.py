from random import choices
from unicodedata import category
from django.db import models

# Create your models here.


class Merchant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='merchant_created_by', null=True)
    updated_by = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='merchant_updated_by', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'merchants'


class Store(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='store_created_by', null=True)
    updated_by = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='store_updated_by', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stores'


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='category_created_by', null=True)
    updated_by = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='category_updated_by', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Item(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    discount_type = models.CharField(max_length=10, choices=(
        ('percent', 'percent'), ('flat', 'flat')), default='percent')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='item_created_by', null=True)
    updated_by = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='item_updated_by', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'items'
