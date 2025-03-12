from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
from django.urls import path
from .views import contact_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
]
