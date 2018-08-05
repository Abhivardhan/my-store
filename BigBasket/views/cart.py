from django.views.generic import ListView, CreateView
from BigBasket.models import Product,Cart
from django.shortcuts import redirect
from django.urls import reverse_lazy
from BigBasket.forms import CartAddProductForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth.mixins import LoginRequiredMixin


class DisplayCart(LoginRequiredMixin, ListView):
	login_url = '/login/'
	model = Cart

	context_object_name = 'cart_data'
	template_name = 'BigBasket/cart/list.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(DisplayCart, self).get_context_data(**kwargs)
		cart = list(Cart.objects.values().filter(user = self.request.user))

		price = 0
		for i in cart:
			product_id = i['products_id']
			product = Product.objects.get(id=product_id)
			price += product.price


		context.update({'total':price})
		return context

	def get_queryset(self):
		return Cart.objects.filter(user = self.request.user)



def add_to_cart(request, product_id, quantity=1):
	if request.user.is_authenticated:

		user = request.user
		product = Product.objects.get(pk=product_id)

		try:
			cart = Cart.objects.get(user = user)
			if product in list(cart):
				pass
			else:
				cost = quantity * product.price
				cart = Cart(user=user, products=product, quantity=quantity, subtotal=cost)
				cart.save()

		except:
			cost = quantity*product.price
			cart = Cart(user = user, products = product, quantity=quantity, subtotal=cost)
			cart.save()

		return redirect("BigBasket:cart")
	else:
		return redirect('BigBasket:login')

def remove_from_cart(request, product_id):
	if request.user.is_authenticated:
		user = request.user
		cart = Cart.objects.get(products = product_id, user = user)
		cart.delete()

		return redirect('BigBasket:cart')
	else:
		return redirect('BigBasket:login')

def clear_cart(request):
	if request.user.is_authenticated:
		user = request.user
		cart = Cart.objects.filter(user = user)
		cart.delete()

		return redirect('BigBasket:cart')
	else:
		return redirect('BigBasket:login')























# from django.views.generic import  ListView
# from BigBasket.models import Cart, Product
# from django.shortcuts import get_object_or_404, redirect, render
#
# class CartList(ListView):
# 	model = Cart
# 	context_object_name = 'cart'
# 	template_name = 'BigBasket/cart/list.html'
# 	import ipdb
# 	ipdb.set_trace()
# 	def get_queryset(self):
# 		user = self.request.user
# 		return Cart.objects.filter(user = user)
#
# 	def get_context_data(self, *, object_list=None, **kwargs):
# 		context = super(CartList,self).get_context_data(**kwargs)
# 		# context.update({'user_permissions': self.request.user.get_all_permissions()})
# 		return context
#
#
# def add_to_cart(request, **kwargs):
#
# 	product_id = kwargs.get('pk')
# 	user = request.user
# 	product = Product.objects.get(id=product_id)
#
# 	item_to_cart = Cart(user=user, products=product, subtotal=product.price, total_items=1)
# 	item_to_cart.save()
#
# 	return redirect('BigBasket:cart')
#
#
# def clear_cart(request):
# 	cart = Cart(request.session)
# 	product =Product.objects.get(id=request.GET.get('id'))
# 	if cart:
# 		cart.delete(product)
# 	else:
# 		cart = Cart(request.session)
# 		cart.save()
# 	return redirect('BigBasket:cart')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
# from BigBasket.models import Product
# from BigBasket.cart import Cart
# from BigBasket.forms import CartAddProductForm
#
# @require_POST
# def cart_add(request, product_id):
# 	cart = Cart(request)
# 	product = get_object_or_404(Product, id=product_id)
# 	form = CartAddProductForm(request.POST)
# 	if form.is_valid():
# 		cd = form.cleaned_data
# 		cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
# 	return redirect('BigBasket:cart_detail')
#
# def cart_remove(request, product_id):
# 	cart = Cart(request)
# 	product = get_object_or_404(Product, id=product_id)
# 	cart.remove(product)
# 	return redirect('BigBasket:cart_detail')
#
# def cart_detail(request):
# 	cart = Cart(request)
# 	for item in cart:
# 		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
# 	return render(request, 'BigBasket/cart/detail.html', {'cart': cart})