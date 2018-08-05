from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

date_of_birth = models.DateField(null=True,blank=True)
mobile_number = models.CharField(max_length=12, null=True)
profile_photo = models.ImageField(null=True)

date_of_birth.contribute_to_class(User, 'date_of_birth')
mobile_number.contribute_to_class(User, 'mobile_number')
profile_photo.contribute_to_class(User, 'profile_photo')

class Category(models.Model):
	name = models.CharField(db_index=True, max_length=100)
	slug = models.CharField(max_length=100, db_index=True, unique=True, null=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_absolute_url(self):
		return reverse('BigBasket:product_list_by_category',args=[self.slug])

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, null=True)
	description = models.TextField(max_length=500, blank=True)
	image = models.ImageField(upload_to='products/', blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	stock = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	class Meta:
		ordering = ('name',)
		index_together = (('id','slug'),)

	def get_absolute_url(self):
		return reverse('BigBasket:product_detail',args=[self.id,self.slug])

	def __str__(self):
		return self.name



class Cart(models.Model):
	user =models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	products = models.ForeignKey(Product,blank=True, on_delete=models.CASCADE)
	subtotal = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)


	def __str__(self):
		return self.products.name



class Checklist(models.Model):
	user = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE)
	products = models.ForeignKey(Product, blank = True, on_delete=models.CASCADE)

	def __str__(self):
		return self.products.name

class Address(models.Model):
	fullname = models.CharField(max_length=64, null=True, blank=True)
	street = models.CharField(max_length=200, null=True, blank=True)
	landmark = models.CharField(max_length=30, null=True, blank=True)
	city = models.CharField(max_length=30, null=True, blank=True)
	pincode=models.CharField(max_length=10, null=True, blank=True)
	state = models.CharField(max_length=30, null=True, blank=True)
	country=models.CharField(max_length=20, null=True, blank=True)
	mobileno=models.CharField(max_length=30, null=True, blank=True)
	address_type=models.CharField(max_length=100, null=True, blank=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def  __str__(self):
		return self.fullname


class Order(models.Model):
	order_number = models.IntegerField(null=True, blank=True)
	product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
	address = models.ForeignKey(Address,null=True, blank=True, on_delete=models.CASCADE)
	user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.product.name