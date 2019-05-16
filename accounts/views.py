from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from checkout.models import OrderLineItem, Order
from features.models import Features



@login_required() 
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    
    user = request.user
    auth.logout(request)
    messages.success(request, 'You have successfully logged out, goodbye {0}'.format(user))
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in, welcome {0}".format(user))

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered, welcome to Nordlander {0}".format(user))
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


@login_required() 
def myFeatures(request):
    """
    Retrieves a list of purchased features by currently logged in user (retireves the feature id's from orders)
    """
    
    myOrders = OrderLineItem.objects.filter(user=request.user.username).order_by('product').values('product').distinct()
    
    myProductIds = []
    
    for id in myOrders:
        myProductIds.append(id['product'])
    
    myFeatures = []
        
    for id in myProductIds:
        feature = get_object_or_404(Features, pk=id)
        myFeatures.append(feature)
    
    return render(request, "myFeatures.html", {"myFeatures": myFeatures})

