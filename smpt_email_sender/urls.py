from . import views
from django.urls import path

urlpatterns = [
    path("", views.send_email, name='home'),
    path("send_email/", views.send_email, name='send_email'),
]