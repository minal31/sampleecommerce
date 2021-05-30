from django.conf.urls import url
from . import views

app_name = 'MyCart'
urlpatterns = [
    #url(r'^$', views.product_list, name='product_list'),
    #url(r'^(?P<category_slug>[-\w]+)/$',views.product_list, name='product_list_by_category'),
    

	url(r'^$', views.cart_detail, name='cart_detail'),
	url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
	url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]


