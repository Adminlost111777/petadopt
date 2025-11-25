from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_view
from . forms import LoginForm, PasswordResetForm

urlpatterns = [
    path('',views.home),
    path('home.html',views.home,name='home'),
    path('blog.html',views.blog,name='blog'),
    path('aboutus.html',views.aboutus,name='aboutus'),
    path('accounts/profile/',views.ProfileView.as_view(), name='profile'),
    path('address/',views.address,name='address'),
    path('updateaddress/<int:pk>',views.updateAddress,name='updateAddress'),
    path('Adoption.html',views.adoption,name='adoption'),
    path('add_adoption/',views.add_adoption,name='add_adoption'),
    path('del_adoption/',views.del_adoption,name='del_adoption'),
    path('logout/',views.userlogout,name='logout'),
    path('del_address',views.del_address,name='del_address'),
    path('search/',views.search,name='search'),
    path('donate.html',views.donate,name='add_donation'),

    # login authentication
    path('customerregistration.html',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('passwordreset.html',auth_view.PasswordResetView.as_view(template_name='app/passwordrest.html',form_class=PasswordResetForm),name='passwordreset'),
]