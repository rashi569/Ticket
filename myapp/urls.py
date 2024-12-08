# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_form_view, name='ticket_form'),
]
