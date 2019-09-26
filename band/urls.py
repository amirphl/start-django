from django.urls import path
from django.views.generic import TemplateView, CreateView

from . import views

urlpatterns = [
    path('home/', views.homepage, name='index'),
    path('protected_view/', views.my_protected_view, name='protected_view'),
    path('login/', views.login, name='login'),
    path('get_login_page/', TemplateView.as_view(template_name='login_page.html'), name='get_login_page'),
    path('register/', views.register, name='register'),
    path('get_register_page/', TemplateView.as_view(template_name='register.html'), name='get_register_page'),
    path('bands/', views.band_listing, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/search/<str:name>', views.band_search, name='band-search'),
]
