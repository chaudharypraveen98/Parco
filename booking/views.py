from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import FormView
from rest_framework.response import Response
from rest_framework.views import APIView

from smart_parking.settings import EMAIL_HOST_USER
from .login import LoginForm
from .serializers import UserSerializer, LoginSerializer, BookingForm


def contact(request):
    return render(request, "booking/contact.html")


class CreateBooking(FormView):
    template_name = "booking/dashboard.html"
    form_class = BookingForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            booking = form.save(self, commit=False)
            booking.booking_id = "PARK" + booking.start_timing.strftime("%d%b%Y%H%M")
            print(booking.booking_id)
            booking.end_timing = booking.start_timing + timedelta(hours=booking.duration)
            msg = f"Thank you for booking with us. Your booking id "
            send_mail(msg, EMAIL_HOST_USER, [booking.email], fail_silently=False)
            messages.success(request, 'Form submission successful')
            booking.save()


def index(request):
    return render(request, "booking/index.html")


class SignUp(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # return Response(({"user": UserSerializer(user, context=self.get_serializer_context()).data,}))
        return Response({"msg": "successfully created"})


class LoginApi(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response({"username": user.get_username()})


class LoginView(FormView):
    form_class = LoginForm
    template_name = "booking/login.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            us = user.username
            print("---------", us)
            if user is not None:
                login(request, user)
                return redirect('booking:create')
                # return render(request, 'booking/dashboard.html', {"user": user})
                # return HttpResponse(json.dumps(user), content_type="application/json")
                # return JsonResponse(us, safe=False)
        return render(request, self.template_name, {"form": form})
