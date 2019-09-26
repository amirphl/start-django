from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import ugettext

from band import models


# Create your views here.


def band_listing(request):
    """A view of all bands."""
    bands = models.Band.objects.all()
    return render(request, 'band_listing.html', {'bands': bands})


def band_detail(request):
    return None


def band_search(request):
    return None


@login_required
def my_protected_view(request):
    """A view that can only be accessed by logged-in users"""
    return render(request, 'protected.html', {'current_user': request.user})


def homepage(request):
    """
    Shows the homepage with a welcome message that is translated in the
    user's language.
    """
    message = ugettext('Welcome to our site!')
    return render(request, 'homepage.html', {'message': message})
