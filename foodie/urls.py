from ast import Div
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meals', views.meals, name='meals'),
    path('mealss/<str:id>/<slug:slug>', views.mealss, name='mealss'),
    path('variety/<str:id>/<slug:slug>', views.variety, name='variety'),
    path('signin', views.signin, name='signin'),
    path('logoutfunc', views.logoutfunc, name='logoutfunc'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('profile', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile_update'),
    path('password-update', views.password_update, name='password-update'),
    path('cart', views.cart, name='cart'),
    path('remove_item', views.remove_item, name='remove_item'),
    path('addtocart', views.addtocart, name='addtocart'),
    path('checkout', views.checkout, name='checkout'),
    path('paid_order', views.paid_order, name='paid_order'),
    path('placeorder', views.placeorder, name='placeorder'),
    path('vary', views.vary, name='vary'),
    path('search', views.search, name='search')
]



