# from django.contrib.auth.models import User
from datetime import datetime

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    images = models.ImageField(blank=None)

    @staticmethod
    def get_all_categories():
        return Categories.objects.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    # to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Назва', max_length=50)
    description = models.TextField('Опис')
    slug = models.SlugField(max_length=200, db_index=True, default='')
    images = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True, null=True,
                               upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Item.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Item.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Item.objects.filter(category=category_id)
        else:
            return Item.get_all_products()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        index_together = (('id', 'slug'),)


class Order(models.Model):
    product = models.ForeignKey(Item,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
