from django.conf.urls import url
from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("create/", views.CreateBooking.as_view(), name="create"),
    path("api/login/", views.LoginApi.as_view(), name="api-login"),
    path("api/signup/", views.SignUp.as_view(), name="api-signup"),
]
