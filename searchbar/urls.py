from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views
app_name = 'searchbar'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('register/', views.register, name= 'register'),
    path('profile/', views.view_profile, name= 'view_profile'),
    path('profile/edit/', views.edit_profile, name= 'edit_profile'),
    path('change-password/', views.change_password, name= 'change_password'),
    path('todaysdeals/', views.todays_deals, name = 'todaysdeals'),
    path('login/', views.loguser, name = 'loguser'),
    path('search/', views.search, name = 'search')
]
