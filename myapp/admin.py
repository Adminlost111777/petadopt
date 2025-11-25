from django.contrib import admin
from .models import Pet, Blog, Customer, Adoption

from .models import Donation

class PetAdmin(admin.ModelAdmin):
    list_display=('name','quantity','id')

class CustomerAdmin(admin.ModelAdmin):
    list_display=('name','user','city','number')

class AdoptionAdmin(admin.ModelAdmin):
    list_display=('owned','pet')
    
class DonationAdmin(admin.ModelAdmin):
    list_display=('donated','user_name')



admin.site.register(Donation)
admin.site.register(Pet)
admin.site.register(Blog)
admin.site.register(Customer)
admin.site.register(Adoption)


# Register your models here.
