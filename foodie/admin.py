from django.contrib import admin
from . models import *
# Register your models here.

class VarietyAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'slug', 'image', 'created', 'updated']
    list_display_links = ('id', 'name', 'slug')
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Variety, VarietyAdmin)


class MealAdmin(admin.ModelAdmin):
    list_display= ('id', 'variety', 'meal', 'slug', 'image', 'spicy', 'time', 'price', 'discount', 'display', 'breakfast', 'lunch', 'dinner', 'updated','min_order','max_order')
    list_display_links = ['id', 'variety', 'meal', 'slug']
    list_editable= ['price', 'discount']
    prepopulated_fields = {'slug':('meal',)}
    
admin.site.register(Meal, MealAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display= ('name', 'phone', 'subject', 'message', 'created', 'status', 'closed', 'remark')
    list_display_links = ('name', 'phone', 'subject')
    
admin.site.register(Contact, ContactAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display= ['user', 'first_name', 'last_name', 'phone', 'address', 'state', 'image']   
    list_display_links = ('user', 'first_name', 'last_name')

admin.site.register(Profile, ProfileAdmin)



