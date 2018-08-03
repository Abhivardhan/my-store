from django.conf.urls import url
from django.urls import path
from BigBasket.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'BigBasket'

urlpatterns = [

	url(r'^login/$', Login.as_view(), name='login'),
	url(r'^signup/$', SignUp.as_view(), name='signup'),
	url(r'^logout/$', logout_view, name='logout'),

	# path("cart",CartList.as_view(),name='cart'),
	# path("cart/add_to_cart/<int:pk>/",add_to_cart,name="add_to_cart"),
    # path("cart/<int:pk>/delete",DeleteCartView.as_view(),name="remove_from_cart"),

	url(r'checklist/$', CheckList.as_view(), name='checklist'),
	url(r'checklist/add/(?P<product_id>\d+)/$', add_to_checklist, name='checklist_add'),
	url(r'checklist/remove/(?P<product_id>\d+)/$',remove_from_checklist,name='remove_checklist'),
	url(r'checklist/clear/$', clear_checklist, name='clear_checklist'),

	url(r'cart/$', DisplayCart.as_view(),name = 'cart'),
	url(r'cart/add/(?P<product_id>\d+)/$', add_to_cart,name = 'add_to_cart'),
	url(r'cart/remove/(?P<product_id>\d+)/$', remove_from_cart,name = 'remove_cart'),
	url(r'cart/clear/$', clear_cart,name = 'clear_cart'),

	# url(r'selectAddress/$', DisplayAddress.as_view(), name='select_address'),
	# path("address/<int:pk>/delete", DeleteAddressView.as_view(), name="address_delete_html"),
	# path("address/<int:pk>/edit", UpdateAddressView.as_view(), name="address_edit_html"),
	# url(r'addAddress/$', AddAddress.as_view(),name='add_address'),

	url(r'selectAddress/$', AddressListView.as_view(), name="select_address"),
    url("address/delete/(?P<address_id>\d+)/$", DeleteAddressView.as_view(), name="delete_address"),
    url("address/edit/(?P<address_id>\d+)/$", UpdateAddressView.as_view(), name="edit_address"),
    url(r'addAddress/$', CreateAddressView.as_view(), name="add_address"),

	url(r'makeOrder/(?P<address_id>\d+)/$', makeOrder, name='make_order'),
	url(r'orders/$', DisplayOrder.as_view(),name="my_orders"),

	url(r'^$', product_list, name='product_list'),
	url(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),

	# url(r'^cart/add/(?P<product_id>\d+)/$', cart_add, name='add_to_cart'),
	# url(r'^cart/', cart_detail, name='cart_detail'),
	#
	# url(r'^cart/remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
				document_root=settings.MEDIA_ROOT)