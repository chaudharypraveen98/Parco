from django.contrib.admin import widgets
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm
from rest_framework import serializers, exceptions

from booking.models import Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        print("hey")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "user is inactive"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Wrong credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both"
            raise exceptions.ValidationError(msg)
        return data


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        exclude =('end_timing',)
