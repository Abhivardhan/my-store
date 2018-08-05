from django.contrib.auth.mixins import LoginRequiredMixin

from BigBasket.models import *
from django.views.generic import CreateView, ListView
from django.shortcuts import redirect, render


class DisplayOrder(LoginRequiredMixin, ListView):
	login_url = '/login/'
	model = Order

	context_object_name = 'order_data'
	template_name = 'BigBasket/order/list.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(DisplayOrder, self).get_context_data(**kwargs)
		return context

	def get_queryset(self):
		return Order.objects.all().filter(user = self.request.user)

def make_payment(request):
	if request.user.is_authenticated:
		cart = Cart.objects.all().filter(user = request.user)
		cart.delete()

		return redirect('BigBasket:my_orders')
	else:
		return redirect('BigBasket:login')

def cancelOrder(request, order_id):
	if request.user.is_authenticated:
		order = Order.objects.all().filter(user = request.user, order_number=order_id)
		order.delete()

		return redirect('BigBasket:cart')
	else:
		return redirect('BigBasket:login')

def makeOrder(request, address_id):
	if request.user.is_authenticated:
		address = Address.objects.get(pk=address_id)
		user = request.user
		order_number = list(Order.objects.values('order_number').filter(user=user))


		count_list = []
		for index in order_number:
			count_list.append(index['order_number'])
		count_list.sort(reverse=True)
		if len(count_list) == 0:
			order_number = 1
		else:
			order_number = count_list[0] + 1


		total_cost = 0
		total_quantity = 0
		cart = list(Cart.objects.all().filter(user=user))
		for item in cart:
			total_cost += item.products.price
			total_quantity += 1
			order = Order(address=address, user=user, product=item.products, order_number=order_number)
			order.save()

		order_data = Order.objects.all().filter(user=request.user, order_number=order_number)

		# cart1 = list(Cart.objects.values().filter(user = request.user))
		# ord_number = Order.objects.all().filter(user = request.user).count()
		# price = 0
		# for i in cart1:
		# 	product_id = i['products_id']
		# 	product = Product.objects.get(id=product_id)
		# 	price += product.price

		return render(request, 'BigBasket/order/payment.html',
					  {'order_data': order_data, 'total_cost': total_cost, 'total_quantity': total_quantity, 'order_number': order_number})
	else:
		return redirect('BigBasket:login')
