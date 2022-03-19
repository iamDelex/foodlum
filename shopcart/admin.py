from django.contrib import admin
from .models import *
# Register your models here.



class ShopcartAdmin(admin.ModelAdmin):
    list_display= ['user','meal','quantity','how_spicey','order_no','item_paid']  
    list_display_links = ('user', 'meal', 'quantity')
    readonly_field = ['user','meal','quantity','how_spicey','order_no','item_paid'] 

admin.site.register(Shopcart, ShopcartAdmin)



class PaidorderAdmin(admin.ModelAdmin):
    list_display= ('user','total','cart_no','payment_code','paid_item','first_name','last_name')  
    list_display_links = ('user', 'total', 'cart_no')
    readonly_field = ('user','total','cart_no','payment_code','paid_item','first_name','last_name')  

admin.site.register(Paidorder, PaidorderAdmin)


class ShippingAdmin(admin.ModelAdmin):
    list_display= ['id','meal','user','shipping_no','paid_cart','fname','lname','address','phone','email','state','status','admin_remark']  
    list_display_links = ('id','meal', 'user')
    readonly_field = ['id', 'user','shipping_no','paid_cart','fname','lname','address','state','phone','email']  

admin.site.register(Shipping, ShippingAdmin)