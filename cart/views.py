from django.shortcuts import render , redirect , get_object_or_404

from .cart import Cart
from product.models import Product , ProductVaraiant
from .forms import AddToProductCart
from product.models import  Colour
# Create your views here.


def detail_cart_view(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_cart'] =  AddToProductCart(initial={'quantity':item['quantity'] , 'inplace':True})

    return render(request , 'cart/detail_view_cart.html' , context={'cart':cart})



def add_cart_view(request , product_id):
    cart = Cart(request)
    product = get_object_or_404(Product , id = product_id)
    form = AddToProductCart(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        inplace = cleaned_data['inplace']
        cart.add(product , quantity , inplace  )

    return redirect('cart:detail_cart')


def delete_from_cart(request , product_id):
    product = get_object_or_404(Product , id = product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:detail_cart')



def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:detail_cart')