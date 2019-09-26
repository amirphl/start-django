from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import ugettext

from band import models
from band.forms import LoginForm, RegisterForm
from band.models import Band


def band_listing(request):
    bands = models.Band.objects.all()
    return render(request, 'band_listing.html', {'bands': bands})


def band_detail(request, band_id):
    try:
        band = models.Band.objects.get(id=band_id)
        return render(request, 'band_detail.html', {'band': band})
    except Band.DoesNotExist:
        raise Http404()


def band_search(request, name):
    bands = models.Band.objects.filter(name=name)
    return render(request, 'band_search.html', {'bands': bands})


@login_required
def my_protected_view(request):
    """A view that can only be accessed by logged-in users"""
    return render(request, 'protected.html', {'username': request.user})


def homepage(request):
    """
    Shows the homepage with a welcome message that is translated in the
    user's language.
    """
    message = ugettext('Welcome to our site!')
    members = models.Member.objects.all()
    bands = models.Band.objects.all()
    return render(request, 'homepage.html',
                  {'message': message, 'bands': bands, 'members': members, 'count': bands.count()})


def login(request):
    username = "not logged in"
    if request.method == "POST":
        print("@" * 70)
        print(request.POST)
        print("@" * 70)
        my_login_form = LoginForm(request.POST)
        if my_login_form.is_valid():
            username = my_login_form.cleaned_data['username']
        return render(request, 'loggedin.html', {"username": username})
    else:
        return redirect('get_login_page')


def register(request):
    if request.method == "POST":
        # print("%" * 70)
        # print(request.POST)
        # print("%" * 70)
        my_register_form = RegisterForm(request.POST)
        if my_register_form.is_valid():
            username = my_register_form.cleaned_data['username']
            password = my_register_form.cleaned_data['password']
            User.objects.create(username=username, password=password)
            return redirect('get_login_page')
        return redirect('get_register_page')
    else:
        return redirect('get_register_page')
