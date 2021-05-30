from django.shortcuts import render,redirect, get_object_or_404
from app1.models import Product

#from app1.form import DetailsForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .form import NewUSerForm
from django.contrib.auth import (
    logout as logout_user,
    login as login_user,
    authenticate,
)
from django.contrib import messages

#from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product
#from .form import CartAddProductForm

#from django.contrib.auth.decorators import login_required
from app1.form import DetailsForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def fetch_data(request):
    product_list=Product.objects.all()


    item_name=request.GET.get('item_name')#item_name=pedigree
    if item_name!='' and  item_name!=None:
        product_list=product_list.filter(name__contains=item_name)


    my_dict={'product_list':product_list}
    return render(request,"home.html",my_dict)



#@login_required(login_url='/login/')
def Buy_Now(request):
    form=DetailsForm()
    my_dict={'form':form}
    return render(request,"detail.html",my_dict)
'''  
def Buy_Now(request):
    form=DetailsForm()
    my_dict={'form':form}
	return render(request,"detail.html",my_dict)
 '''


def signup_view(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #return redirect('app1:fetch_data')
            return render(request,"home.html")
    else:
        form = NewUSerForm()
    return render(request, 'signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            #return redirect('app1:fetch_data')
            return render(request,"home.html")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })




def logout(request):
    logout_user(request)
    #return render(request,"logout.html")
    messages.info(request, 'You\'ve been successfully logged out!')
    return redirect('app1:fetch_data')
   # return render(request,"home.html",my_dict)


def order(request):
    order_amount = 50000
    order_currency = '$'
    client=razorpay.Client(auth=('rzp_test_AUvbKnCMO8ysj3','WM7pJyHeQfN5LqTGpOW3oUDb'))

    client.order.create(amount=order_amount, currency=order_currency)

def success(request):
    return render(request,"success.html")

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')
# Create your views here.

