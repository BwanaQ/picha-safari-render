import uuid
from django.db import models
from django.conf import settings
from photo.models import Photo

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        total=0
        cart_items = self.cartItems.all()
        total = sum([item.price for item in cart_items])
        return (round(float(total),2))
    @property
    def vat(self):
        total=0
        cart_items = self.cartItems.all()
        total = sum([item.price for item in cart_items])
        vat = 0.16 * float(total)
        return (round(vat, 2))
    
    @property
    def final_price(self):
        total=0
        cart_items = self.cartItems.all()
        total = sum([item.price for item in cart_items])
        vat = 0.16 * float(total)
        final_price = float(total)+vat
        return (round(final_price,2))
    
    @property
    def tally(self):
        cart_items = self.cartItems.all()
        total = sum([item.quantity for item in cart_items])
        return total    
class CartItem(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='Items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartItems')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.quantity} x {self.photo.title} in cart # {self.cart.id}" )
    
    @property
    def price(self):
        new_price = self.photo.price * self.quantity
        return new_price

