from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'

class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodTypes
        fields = '__all__'

class DonationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationHistory
        fields = '__all__'


class DonationModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationModes
        fields = '__all__'


class DonationRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationReg
        fields = '__all__'


class DonationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = '__all__'


class DonationsDonationModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationsDonationModes
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venues
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'


class SubscriptionModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionMode
        fields = '__all__'


class UserEventSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEventSubscription
        fields = '__all__'

class BloodTypeCompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodTypeCompatibility
        fields = '__all__'


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'


