from django.urls import path
from cart.views import index, add_to_cart, cart, checkout, remove_from_cart 
""",payment_checkout"""
urlpatterns = [
    path('', index, name='cart-home'),
    path('add_to_cart', add_to_cart, name='add'),
    path('remove_from_cart', remove_from_cart, name='remove'),
    path('cart', cart, name='cart'),

    path('checkout', checkout, name='checkout'),
    # path('payment', payment_checkout, name='payment'),

]