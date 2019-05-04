from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_cart(request):
    """
    A View that renders the cart contents page
    """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Add a specified product to the cart, always only adds 1
    """
   
    quantity = 1
    
    cart = request.session.get('cart', {})
    
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 
    
    request.session['cart'] = cart
    return redirect(reverse('features'))


def delete_cart_item(request, id):
    """
    Allows users to delete an item from their cart.
    """
    quantity = int(request.POST.get('delete_button'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
     
    
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))