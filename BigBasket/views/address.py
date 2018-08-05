from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from  BigBasket.models import Address
from BigBasket.forms import *
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django import forms
from django.shortcuts import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
class AddressListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model =Address
    context_object_name = 'address'
    template_name = "BigBasket/address/list.html"

    def get_context_data(self, **kwargs):
        context = super(AddressListView, self).get_context_data(**kwargs)
        user = self.request.user

        print(type(user))
        address = list(
            Address.objects.values('id', 'country', 'fullname','mobileno','pincode','city','street',
             'landmark','state' ,'address_type').filter(user_id=user.id))

        context.update({
            'address_data': address,
        })
        return context


from django.views.generic.edit import CreateView
class CreateAddressView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Address
    form_class = AddressForm
    template_name = 'BigBasket/user/address_form.html'

    def get_context_data(self, **kwargs):
        context = super(CreateAddressView, self).get_context_data(**kwargs)
        context.update({'address_form': context.get('form')})
        return context
    def post(self, request, *args, **kwargs):
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address = address_form.save(commit=False)
            address.user = request.user
            address.save()
        return redirect('BigBasket:select_address')
#
# class UpdateAddressView(LoginRequiredMixin,UpdateView):
#     login_url = '/login/'
#     model = Address
#     form_class = AddressForm
#     template_name = 'BigBasket/user/address_form.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(UpdateAddressView, self).get_context_data(**kwargs)
#         address_form = context.get('address')
#         context.update({'address_form': context.get('form')})
#         return context
#
#     def post(self, request, *args, **kwargs):
#         address = Address.objects.get(pk=kwargs.get('pk'))
#         form = AddressForm(request.POST, request.FILES, instance=address)
#         form.save()
#         return redirect('BigBasket:select_address')
#


# class DeleteAddressView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
#     model = Address
#     template_name = 'BigBasket/user/del_address_form.html'
#     success_url = reverse_lazy('BigBasket:select_address')
#
#     def has_permission(self):
#         user_id = self.request.user.id
#         check_user = Address.objects.get(pk=self.kwargs['pk']).user.id
#
#         if not user_id == check_user:
#             self.raise_exception = True
#             success_url = reverse_lazy('BigBasket:select_address')
#             return False
#         else:
#             def get(self, request, *args, **kwargs):
#                 return self.post(request, args, kwargs)
#
#             success_url = reverse_lazy('BigBasket:select_address')
#             return True
#
