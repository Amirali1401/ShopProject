from django.shortcuts import render , get_object_or_404 , redirect , reverse
from django.contrib.auth.decorators import login_required

from .models import Order , OrderItem
from .forms import OrderForm , OrderwayForm
from cart.cart import Cart
# Create your views here.

@login_required()
def order_view(request):
    orders =  Order.objects.all()
    return render(request , 'order/order.html' , context={'orders':orders} )


@login_required()
def order_create_view(request):
    form = OrderForm(request.POST)
    cart = Cart(request)
    if len(cart)==0:
        return redirect('cart:detail_cart')

    if form.is_valid():
        form_obj = form.save(commit=False)
        form_obj.user = request.user
        form_obj.save()
        for item in cart:
            product = item['product_obj']
            OrderItem.objects.create(
                order=form_obj,
                product=product,
                quantity=item['quantity'],
                price=product.selling_price,
            )

        cart.clear()
        request.user.first_name = form_obj.first_name
        request.user.last_name = form_obj.last_name
        request.user.save()
        request.session['order_id'] = form_obj.id
        return redirect('order:checkout')

    return render(request, 'order/order_create.html', context={'form': form  })




@login_required()
def checkout_view(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order , id = order_id)
    return render(request , 'order/checkout.html' , context={'order':order  })
