from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Pet,Blog ,Customer,Adoption
from . forms import CustomerRegistrationForm,ProfileForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Donation


class CustomerRegistrationView(View):
    def get(self,request):
        form= CustomerRegistrationForm()
        return render(request,'customerregistration.html',locals())
    def post(self,request):
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
            return redirect('/accounts/login/')
        else:
            messages.warning(request,"Invalid Input Data")
            return render(request,'customerregistration.html',locals())
        

class ProfileView(View):
    def get(self,request):
        form =ProfileForm()
        return render(request,'profile.html',locals())
    def post(self,request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user= request.user
            name =form.cleaned_data['name']
            number =form.cleaned_data['number']
            city = form.cleaned_data['city']

            reg= Customer(user=user,name=name, city=city, number=number)
            reg.save()
            messages.success(request,"Congratulations!Profile saved")
            return redirect('/address',locals())

        else:
            messages.warning(request,"Invalid data")
            return redirect('/profile.html',locals())

@login_required        
def address(request):
    add= Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())

@login_required 
class updateAddress(View):
    def get(self,request,pk):
        add =Customer.objects.get(pk=pk)
        form =ProfileForm(instance=add)
        return render(request,'updateaddress.html',locals())
    def get(self,request,pk):
        form= ProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name =form.cleaned_data['name']
            add.number =form.cleaned_data['number']
            add.city = form.cleaned_data['city']
            add.save()
            messages.success(request,"Congratulations!Profile saved")
            return redirect('login.html')
        else:
            messages.warning(request,"Invalid data")
            return redirect(request,'customerregistration.html',locals())

        return render(request,'updateaddress.html',locals())
    
def login(request):
    return redirect('/home.html')

def donate(request):
    return render(request,'donate.html')
    
def home(request):
    pet =Pet.objects.all
    return render(request,'home.html',{'pet':pet})

def blog(request):
    blog = Blog.objects.all
    return render(request,'blog.html',{'blog':blog})

def aboutus(request):
    return render(request,'aboutus.html')


@login_required
def adoption(request):
    adoptions = Adoption.objects.filter(owned=request.user).all()
    return render(request,'Adoption.html', {'adoptions': adoptions})


@login_required
def add_adoption(request):
    pet_pk = request.POST.get('pk')
    pet= Pet.objects.get(pk=pet_pk)
    pet.quantity -= 1
    pet.save()
    Adoption.objects.create(owned=request.user,pet=pet)
    return redirect('/Adoption.html')

def add_donation(request):
    amount = request.POST.get('amount')
    Donation.objects.create(username=request.user, donated=amount)
    return redirect('/donate.html')
    


@login_required
def del_adoption(request):
    adoption_pk = request.POST.get('pk')
    adoption = Adoption.objects.get(pk=adoption_pk,owned=request.user)
    pet=adoption.pet
    pet.quantity += 1
    pet.save()
    adoption.delete()
    return redirect('/Adoption.html')

@login_required
def userlogout(request):
    logout(request)
    return redirect('/customerregistration.html')

@login_required 
def del_address(request):
    address_pk =request.POST.get('pk')
    print(address_pk)
    address =Customer.objects.get(pk=address_pk)
    address.delete()
    return redirect('/address/')


def search(request):
    query = request.GET.get("q", "")
    pets = Pet.objects.filter(species__icontains=query).all() if query else Pet.objects.all()

    return render(request, "home.html", {"pet": pets,"query": query})
# Create your views here.
