from BigBasket.models import *
from django.views.generic import CreateView, ListView
from django.shortcuts import redirect


class DisplayOrder(ListView):
	model = Cart

	context_object_name = 'order_data'
	template_name = 'BigBasket/order/list.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(DisplayOrder, self).get_context_data(**kwargs)
		return context

def makeOrder(request, address_id):
	address = Address.objects.get(pk=address_id)
	user = request.user
	cart = None
	order = Order(address=address, cart=cart, total=1)
	order.save()

	return redirect("BigBasket:my_orders")