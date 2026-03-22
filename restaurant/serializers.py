from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    booking_date = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = '__all__'
