from product.models import Product


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product , quantity=0, replace_current_quantity=False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
            }

        if replace_current_quantity:
            self.cart[product_id] = {
                'quantity': quantity,
            }

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]

        self.save()

    def __iter__(self):
        products_id = self.cart.keys()
        products = Product.objects.filter(id__in=products_id)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['quantity'] * item['product_obj'].selling_price
            yield item


    def get_total_price(self):

        sum_price =  sum(item['product_obj'].selling_price * item['quantity'] for item in self)
        return sum_price


    def calculate_pure_price(self):
        sum_price = sum(item['product_obj'].selling_price * item['quantity'] for item in self.cart.values())
        return (sum_price - (100000 + 4000))

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']

        self.save()
