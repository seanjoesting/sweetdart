from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
import time
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import *
import requests
import json

from .forms import (
    RegistrationForm,
    EditProfileForm,
    LoginForm
)


def loguser(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('searchbar:index'))
    else:
        form = LoginForm()
        args = {'form': form}
        return render(request, 'login.html', args)


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('searchbar:index'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'reg_form.html', args)
def todays_deals(request):
    return render(request, 'todaysdeals.html')

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('view_profile'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)

def index(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        print(search_query)
    return render(request, 'index.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        q = q.replace(' ', '&search=' )
        url = 'https://api.bestbuy.com/v1/products((search='
        url = url + q + '))?apiKey=8ajgaRE2wV0CCIh7FAvUFGTT&sort=salePrice.asc&show=salePrice,image,url,name,description&pageSize=70&format=json'
        response = requests.get(url)
        products = response.json()
        q = q.replace('&search=' , ' ')
        return render(request, 'products.html', {'results': products, 'query': q})
    return render(request, 'index.html')


