from django.views import View
from django.views.generic import ListView
from BigBasket.models import Product, Checklist
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

class CheckList(ListView):
	model = Checklist
	context_object_name = 'checklist_data'
	template_name = 'BigBasket/checklist/list.html'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(CheckList, self).get_context_data(**kwargs)

		return context

def add_to_checklist(request, product_id):
	user = request.user
	product = Product.objects.get(pk=product_id)

	try:
		checklist = Checklist.objects.get(products = product)
	except:
		checklist = Checklist(user = user, products = product)
		checklist.save()

	return redirect("BigBasket:checklist")

def remove_from_checklist(request, product_id):

	checklist = Checklist.objects.get(products = product_id)
	checklist.delete()


	return redirect('BigBasket:checklist')

def clear_checklist(request):
	user = request.user

	checklist = Checklist.objects.filter(user = user)
	checklist.delete()

	return redirect('BigBasket:checklist')