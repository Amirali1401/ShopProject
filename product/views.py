from django.shortcuts import  get_object_or_404 , render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Product , Category , Wishlist , ProductVaraiant , Colour , Shop , Comment , Notification
from cart.forms import AddToProductCart
from cart.cart import Cart
from .forms import ProductForm , CommentForm

# Create your views here.


#product options and shops
@login_required()
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    shops = Shop.objects.all()
    return render(request , 'product/index.html' , context={'products':products , 'categories':categories , 'shops':shops})



@login_required()
def products_category(request , category_id):
       categories = Category.objects.all()
       category = get_object_or_404(Category , id = category_id)
       products_category = Product.objects.filter(category=category)
       return render(request , 'product/list_category_products.html' , context={'products':products_category , 'categories':categories})


@login_required()
def detail_products_views(request , product_id):
       product = get_object_or_404(Product , id = product_id)
       comments = product.comments.all()
       products_varient = product.product_Varaiant_item.all()
       form = AddToProductCart()
       comment_form  = CommentForm()

       return render(request , 'product/detail_products_view.html' , context={'products':product ,  'form':form , 'products_varient' : products_varient , 'comments':comments , 'comment_form':comment_form})



def shop_view(request  ,shop_id):
    categories = Category.objects.all()
    shop = get_object_or_404(Shop , id = shop_id)
    products = Product.objects.filter(shop = shop)
    return  render(request , 'product/shop_product.html' , context={'categories':categories , 'shop':shop , 'products':products})

#wishlist views


@login_required()
def wishlist_views(request):
   wishlist_products = Wishlist.objects.all()
   return render(request , 'product/wishlist_products.html' , context={'wishlist_products':wishlist_products})



@login_required()
def add_to_wishlist(request , product_id):
    product = get_object_or_404(Product , id = product_id)
    wishlist_item,created = Wishlist.objects.get_or_create(user = request.user , product = product )
    return redirect('product:wishlist_products')



def delete_from_wishlist(request , product_id):
    Wishlist.objects.filter(product = product_id).delete()
    return redirect('product:wishlist_products')


# comment products
class CreateCommentView(LoginRequiredMixin,generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
          form_obj = form.save(commit=False)
          form_obj.user = self.request.user
          product_id = int(self.kwargs['product_id'])
          product = get_object_or_404(Product , id = product_id)
          form_obj.product = product
          return super().form_valid(form)



#About Notification
class ListViewNotifications(generic.ListView):
    model = Notification
    template_name = 'product/notification.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.all()



#search for products
class SearchResultList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/index.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Product.objects.filter(
            Q(name__incontain=query) | Q(description_icontains=query)
        )