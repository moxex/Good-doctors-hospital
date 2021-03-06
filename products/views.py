from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
from .models import Category, Product, Order, OrderItem
from cart.forms import CartAddProductForm
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from .render import Render



# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {
        'category': category, 
        'categories':categories, 
        'products': products,
    }
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/shop_list.html', context)


def product_detail(request, id, slug):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product':product, 
        'category': category, 
        'categories': categories, 
        'products': products, 
        'cart_product_form': cart_product_form
    }
    return render(request, 'products/shop_details.html', context)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            
            # clear the cart
            # cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            context = {
                'order': order,
                'cart': cart,
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone_number']
            }
            return render(request, 'products/pay_with_paystack.html', context)
    else:
        form = OrderCreateForm()
    return render(request, 'products/create.html', {'cart': cart, 'form': form})


def product_category(request, category):
    product = Product.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-date'
    )
    context = {
        "category": category,
        "product": product,
    }
    return render(request, "products/category_product_list.html", context)


def ajax_payment(request):
    if request.is_ajax():
        reference_id = request.POST.get('reference')
        x = Order(reference=reference_id, paid=True)
        x.save()
        if x:
            response = {
                'message': "Your Payment was successfully received"
            }
            return JsonResponse(response)
        else:
            response = {
                'message': "Your Payment Failed"
            }
            return JsonResponse(response)


# view for pdf rendering
class Pdf(View):

    def get(self, request, id):
        cart = Cart(request)
        order_item = get_object_or_404(Order, id=id)
        today = timezone.now()
        # clear the cart
        cart.clear()
        params = {
            'id': id,
            'today': today,
            'cart': cart,
            'order_item': order_item,
            # 'request': request
        }
        return Render.render('products/pdf.html', params)
