import uuid
import json
import requests


from ast import Return
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
from foodie.models import *
from shopcart.models import *
from foodie.forms import *


def index(request):
    breakfast = Meal.objects.filter(breakfast=True, display=True).order_by('-id')[:4]
    lunch = Meal.objects.filter(lunch=True, display=True).order_by('-id')[:4]
    dinner = Meal.objects.filter(dinner=True, display=True).order_by('-id')[:4]
    varieties = Variety.objects.all()
    
    
    
    
    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'varieties': varieties
    }
    
    return render(request, 'index.html', context)
    
@login_required(login_url='signin')
def meals(request):
    if 'search' in request.GET:
        searched = request.GET ['search']
        meals = Meal.objects.filter(Q(Q(meal__icontains=searched)|Q(time__icontains=searched)))
    else:
        meals = Meal.objects.all()
    
    
    
    context = {
       'meals':meals,
       
    }
    
    return render(request, 'meals.html', context)
 
def mealss(request, id, slug):
     mealss = Meal.objects.get(pk=id)
     
     
     context = {
         'mealss':mealss,
         
     }
     
     return render(request, 'mealss.html', context)
 
 
def variety(request, id,slug):
    variety = Meal.objects.filter(variety_id=id) #query for single variety and it children
    single_variety = Variety.objects.get(pk=id)  #query for single variety only
    
    
    context = {
       'variety' : variety,
       'single' : single_variety,
       
    }
    
    return render(request, 'variety.html',context)

def vary(request):
    varieties = Variety.objects.all()
    
    
    context = {
        
       'varieties':varieties
    }
    
    return render(request, 'vary.html',context)


def contact(request):
    cform = ContactForm() # instatiate an empty form for a GET request
    if request.method == 'POST':
        cform = ContactForm(request.POST) # instatiate the form for a POST request
        if cform.is_valid():
            cform.save()
            messages.success(request, 'Thank you for contacting us! our customer care agent will reach you soon')
        return redirect('index')
    
    context = {
        'cform' : cform
    }
    return render('index.html', context)

def profile(request):
    profile = Profile.objects.get(user__username= request.user.username)
    
    
    context = {
        'profile':profile,
        
    }
    
    return render(request, 'user_profile.html', context)

#authentication

def signin(request):
    #making a post request
    if request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            messages.success(request, f' Dear {user.first_name}, Welcome to Foodlum')
            return redirect('index')
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect('signin')
            
    return render(request, 'login.html')

def logoutfunc(request):
    logout(request)
    return redirect( 'signin')

def signup(request):
    form = SignupForm() #instantiate the SignupForm for a Get request
    if request.method == 'POST': #check if a post method for persisting data to the DB
        phone = request.POST['phone']
        image = request.POST['image']
        form = SignupForm(request.POST) # instantiate the SignupForm for a POST request
        if form.is_valid(): # ensure security checks here
           user = form.save() # save data if data is valid
           profile = Profile(user = user) # 1st profile is representing the profile models
           profile.first_name = user.first_name
           profile.last_name = user.last_name
           profile.phone = phone
           profile.image = image
           profile.save()
           messages.success(request, 'Signup Successful')
           login(request, user)
           return redirect('index') #send user in to any page you desire, in this case home page
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    
    context = {
        'form':form
    }
    
    
    return render(request, 'signup.html', context)

@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user__username= request.user.username)
    
    
    context = {
        
    'profile':profile,
    
    }
    
    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def profile_update(request):
    load_profile = Profile.objects.get(user__username= request.user.username)
    form = ProfileForm(instance= request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance= request.user.profile)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Dear {user.first_name} your profile update is successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profile')
    
    
    context = {
        'load_profile':load_profile,
        'form':form
    }
    
    
    return render(request, 'profile_update.html', context)

# ,update_session_auth_hash,login_required
@login_required(login_url='signin')
def password_update(request):
    load_profile = Profile.objects.get(user__username= request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f'Dear {user.first_name}, your password update is successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('password-update')
    
    context = {
        'load_profile':load_profile,
        'form':form
    }
    return render (request, 'password_update.html', context)



def addtocart(request):
    # cart_code = str(uuid.uuid4())
    cartno = Profile.objects.get(user__username=request.user.username)
    cart_code = cartno.cart_code
    if request.method == 'POST':
        addquantity = int(request.POST['quantity'])
        addid = request.POST['mealid']
        mealid = Meal.objects.get(pk=addid)
        addspicy = request.POST.get('how_spicey', None)
        
        # Instantiate the cart for prospective users
        cart = Shopcart.objects.filter(user__username=request.user.username, item_paid=False)
        if cart: # Instantiate the cart for a selected item
            more = Shopcart.objects.filter(meal_id=mealid.id, user__username=request.user.username).first()
            if more:
                more.quantity += addquantity
                more.how_spicey += addspicy
                more.save()
                messages.success(request, 'Item added to 🛒')
                return redirect('addtocart')
            else: #add new items
                newitem = Shopcart()
                newitem.user = request.user
                newitem.meal = mealid
                newitem.quantity = addquantity
                newitem.how_spicey = addspicy
                newitem.order_no = cart_code
                newitem.item_paid = False
                newitem.save()
                messages.success(request, 'Item added to 🛒')
                return redirect('addtocart')
                
        else: # create a cart
            newcart = Shopcart()
            newcart.user = request.user
            newcart.meal = mealid
            newcart.quantity = addquantity
            newcart.how_spicey = addspicy
            newcart.order_no = cart_code
            newcart.item_paid = False
            newcart.save()
            messages.success(request, 'Item has been added to your cart!')
    
    return redirect('meals')



def cart(request):
    shopcart = Shopcart.objects.filter(user__username = request.user.username, item_paid=False)
    
    
    subtotal = 0
    vat = 0
    total = 0
    
    for item in shopcart:
        if item.meal.discount:
            subtotal += int(item.meal.discount) * item.quantity
        else:
           subtotal += int(item.meal.price) * item.quantity
    # vat is at 7.5% of the subtotal, i.e 7.5/100 * subtotal
    vat = 0.075 * subtotal
    # addition of vat and subtotal gives the total value to be charged
    total = subtotal + vat
    
    
    context = {
        'shopcart':shopcart,
        'subtotal':subtotal,
        'vat':vat,
        'total':total,
        
    }
    
    return render (request, 'cart.html', context)


#delete item from shopcart
def remove_item(request):
    deleteitem = request.POST['deleteitem']
    Shopcart.objects.filter(pk=deleteitem).delete()
    messages.success(request, 'Item successfully removed from your Cart')
    return redirect('meals')



def checkout(request):
    profile = Profile.objects.get(user__username= request.user.username)
    shopcart = Shopcart.objects.filter(user__username = request.user.username, item_paid=False)
    
    
    
    
    subtotal = 0
    total = 0
    
    for item in shopcart:
        if item.meal.discount:
            subtotal += int(item.meal.discount) * item.quantity
        else:
           subtotal += int(item.meal.price) * item.quantity 
    # vat is at 7.5% of the subtotal, i.e 7.5/100 * subtotal
    vat = 0.075 * subtotal
    # addition of vat and subtotal gives the total value to be charged
    total = subtotal + vat
    
    
    context = {
        'shopcart':shopcart,
        'total':total,
        'profile':profile,
        # 'orderno':shopcart[0].order_no,
        
    }
    
    
    return render(request, 'billing.html', context)


#http://localhost:8000/paid_order
def paid_order(request):
    profile = Profile.objects.get(user__username= request.user.username)
    cart = Shopcart.objects.filter(user__username = request.user.username, item_paid=False)
    for item in cart:
        item.item_paid = True
        item.save()
    
    context = {
        'profile':profile
    }
    return render(request, 'paid_order.html', context)

# shopcart done

# intergrate to payment gate way, in this instance paystack
def placeorder(request):
    
    if request.method == 'POST':
        
        
        
        
        # collect data to send to paystack
        # the api_key(application programming interface key) and curl (call url) will be sourced from paystack site,
        # paystack will give test  secret key for testing, when you want to go live paystack will give the live key
        # cburl (callback url), total, ref_number,order_num, email provided by me in my application,
        api_key = 'sk_test_728b856f01a2849f148286c26ca2dcdc61870fbd'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://54.204.95.186/paid_order'
        # cburl = 'http://localhost:8000/paid_order'
        ref_num = str(uuid.uuid4())
        total = float(request.POST['get_total']) * 100
        cartno = Profile.objects.get(user__username=request.user.username)
        order_num = cartno.cart_code
        # order_num = request.POST['get_orderno']
        address = request.POST['address']
        # phone = request.POST['phone']
        # state = request.POST['state']
        user = User.objects.get(username = request.user.username)
        
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference':ref_num, 'order_number':order_num, 'amount':int(total), 'callback_url':cburl, 'email':user.email, 'currency':'NGN'}
        # collect data to send to paystack done
        # if currency is not stated the default is dollar
        
        
        # call to paystack
        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Network busy, please refresh and try again. Thank you')
        else:
            transback = json.loads(r.text)
            rd_url = transback['data']['authorization_url']
            
            # take record of transaction made
            # cart = Shopcart.objects.filter(user__username= request.user.username, item_paid=False)
            paidorder = Paidorder()
            paidorder.user = user
            paidorder.total = total/100
            paidorder.cart_no = order_num
            paidorder.payment_code = ref_num
            paidorder.paid_item = True
            paidorder.first_name = user.first_name
            paidorder.last_name = user.last_name
            paidorder.save()
            
            shipping = Shipping()
            shipping.user = user
            shipping.shipping_no = order_num
            shipping.paid_cart = True
            shipping.fname = user.first_name
            shipping.lname = user.last_name
            # shipping.address = user.profile.address
            shipping.phone = user.profile.phone
            shipping.state = user.profile.state
            
            shipping.save()
            # take record of transaction made done
            return redirect(rd_url)
        # call to paystack done, when transaction is succesful it redirects to the callback page
        
    # if transaction error occurs it redirects to checkout
    return redirect('checkout')


# def search(request):
#     if request.method== 'GET':
#         search = request.GET.get('search')
#         post = Meal.objects.all().filter(meal=search)
        
        
#         context = {
#             'post':post
#         }
        
#         return render(request, 'search.html', context)
    
    
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        post = Q(Q(meal__icontains=search)|Q(time__icontains=search))
        post = Meal.objects.filter(meal__icontains=search)
    else:
        post = Meal.objects.all()    
        
    context = {
        'post':post
    }
    
    return render(request, 'search.html', context)
       