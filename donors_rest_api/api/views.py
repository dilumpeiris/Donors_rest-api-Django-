from django.contrib.auth.models import User
from .serializers import *
from .models import *

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def apiRoot(request):
    api_root = {
        'Status': 200
    }

    return Response(api_root)


# Users
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((SessionAuthentication, BasicAuthentication,))
def userCreate(request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            username = serializer.data['username']
            email = serializer.data['email']
            password = serializer.data['password']

            user = User.objects.create_user(username, email, password)
            user.save()
            token = Token.objects.create(user=user)

            return Response(serializer.data)
        else:
            return Response('Not Valid')


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((SessionAuthentication, BasicAuthentication,))
def users(request, pk=None):
    if request.method == 'GET' and pk is None:
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        user = Users.objects.get(user_id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk:
        user = Users.objects.get(user_id=pk)
        auth_username = user.username
        auth_email = user.email

        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            username = serializer.data['username']
            email = serializer.data['email']
            password = serializer.data['password']

            auth_user = User.objects.get(username=auth_username, email=auth_email)

            if username:
                auth_user.username = username
            if email:
                auth_user.email = email
            if password:
                auth_user.password = password
                
            auth_user.save()

            return Response(serializer.data)

        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        user = Users.objects.get(user_id=pk)
        auth_username = user.username
        auth_email = user.email
        user.delete()
        User.objects.filter(username=auth_username, email=auth_email).delete()

        return Response('User Deleted')


# Districts
@api_view(['GET', 'POST', 'DELETE'])
def districts(request, pk=None):
    if request.method == 'GET' and pk is None:
        district = Districts.objects.all()
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        district = Districts.objects.get(district_id=pk)
        serializer = DistrictSerializer(district, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Not Valid")

    if request.method == 'POST' and pk:
        district = Districts.objects.get(district_id=pk)
        serializer = DistrictSerializer(instance=district, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Not Valid")

    if request.method == 'DELETE' and pk is None:
        district = Districts.objects.get(district_id=pk)
        district.delete()
        return Response('District Successfully Deleted')


# Cities
@api_view(['GET', 'POST', 'DELETE'])
def cities(request, pk=None):
    if request.method == 'GET' and pk is None:
        cities = Cities.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        city = Cities.objects.get(city_id=pk)
        serializer = CitySerializer(city, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        city = Cities.objects.get(city_id=pk)
        serializer = CitySerializer(instance=city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        city = Cities.objects.get(city_id=pk)
        city.delete()
        return Response('City Successfully Deleted')


# Donation_History
@api_view(['GET', 'POST', 'DELETE'])
def donationHistory(request, pk=None):
    if request.method == 'GET' and pk is None:
        donation_history = DonationHistory.objects.all()
        serializer = DonationHistorySerializer(donation_history, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        donation_history_item = DonationHistory.objects.get(donation_history_item_id=pk)
        serializer = DonationHistorySerializer(donation_history_item, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = DonationHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        donation_history_item = DonationHistory.objects.get(donation_history_item_id=pk)
        serializer = DonationHistorySerializer(instance=donation_history_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE' and pk:
        donation_history_rec = DonationHistory.objects.get(donation_history_item_id=pk)
        donation_history_rec.delete()
        return Response('History item Successfully Deleted')


# Donation_Modes
@api_view(['GET', 'POST', 'DELETE'])
def donationModes(request, pk=None):
    if request.method == 'GET' and pk is None:
        donation_modes = DonationModes.objects.all()
        serializer = DonationModeSerializer(donation_modes, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        donation_modes = DonationModes.objects.get(donation_mode_id=pk)
        serializer = DonationModeSerializer(donation_modes, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = DonationModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        donation_mode = DonationModes.objects.get(donation_mode_id=pk)
        serializer = DonationModeSerializer(instance=donation_mode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        donation_mode = DonationModes.objects.get(donation_mode_id=pk)
        donation_mode.delete()
        return Response('DonationMode Successfully Deleted')


# Donation_Reg
@api_view(['GET', 'POST', 'DELETE'])
def donationReg(request, pk=None):
    if request.method == 'GET' and pk is None:
        donation_regs = DonationReg.objects.all()
        serializer = DonationRegSerializer(donation_regs, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        donation_regs = DonationReg.objects.get(donation_reg_id=pk)
        serializer = DonationRegSerializer(donation_regs, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = DonationRegSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        donation_reg_item = DonationReg.objects.get(donation_reg_id=pk)
        serializer = DonationRegSerializer(instance=donation_reg_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        donation_mode = DonationReg.objects.get(donation_reg_id=pk)
        donation_mode.delete()
        return Response('DonationReg Successfully Deleted')


# Donation_Req
@api_view(['GET', 'POST', 'DELETE'])
def donationRequests(request, pk=None):
    if request.method == 'GET' and pk is None:
        donation_reqs = Requests.objects.all()
        serializer = DonationRequestSerializer(donation_reqs, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        donation_reqs = Requests.objects.get(request_id=pk)
        serializer = DonationRequestSerializer(donation_reqs, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = DonationRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        donation_req_item = Requests.objects.get(request_id=pk)
        serializer = DonationRequestSerializer(instance=donation_req_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        donation_req = Requests.objects.get(request_id=pk)
        donation_req.delete()
        return Response('Donation Request Successfully Deleted')


# Donations
@api_view(['GET', 'POST', 'DELETE'])
def donations(request, pk=None):
    if request.method == 'GET' and pk is None:
        donation = Donations.objects.all()
        serializer = DonationSerializer(donation, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        donation = Donations.objects.get(donation_id=pk)
        serializer = DonationSerializer(donation, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        donation = Donations.objects.get(donation_id=pk)
        serializer = DonationSerializer(instance=donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        donation = Donations.objects.get(donation_id=pk)
        donation.delete()
        return Response('Donation Successfully Deleted')


# Donations_Donation_Mode
@api_view(['GET', 'POST', 'DELETE'])
def donationsDonationModes(request, pk=None):
    if request.method == 'GET' and pk is None:
        donations_donation_modes = DonationsDonationModes.objects.all()
        serializer = DonationsDonationModeSerializer(donations_donation_modes, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        donations_donation_modes = DonationsDonationModes.objects.get(donations_donation_modes_id=pk)
        serializer = DonationsDonationModeSerializer(donations_donation_modes, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = DonationsDonationModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        donations_donation_mode = DonationsDonationModes.objects.get(donations_donation_modes_id=pk)
        serializer = DonationsDonationModeSerializer(instance=donations_donation_mode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        donations_donation_mode = DonationsDonationModes.objects.get(donations_donation_modes_id=pk)
        donations_donation_mode.delete()
        return Response('Donations Donation Mode Successfully Deleted')


# Events
@api_view(['GET', 'POST', 'DELETE'])
def events(request, pk=None):
    if request.method == 'GET' and pk is None:
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        events = Events.objects.get(event_id=pk)
        serializer = EventSerializer(events, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        event = Events.objects.get(event_id=pk)
        serializer = EventSerializer(instance=event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        event = Events.objects.get(event_id=pk)
        event.delete()
        return Response('Event Successfully Deleted')


# Event_Type
@api_view(['GET', 'POST', 'DELETE'])
def eventType(request, pk=None):
    if request.method == 'GET' and pk is None:
        event_types = EventType.objects.all()
        serializer = EventTypeSerializer(event_types, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        event_types = EventType.objects.get(event_type_id=pk)
        serializer = EventTypeSerializer(event_types, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = EventTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        event_type = EventType.objects.get(event_type_id=pk)
        serializer = EventTypeSerializer(instance=event_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        event_type = EventType.objects.get(event_type_id=pk)
        event_type.delete()
        return Response('Event Type Successfully Deleted')


# Organizations
@api_view(['GET', 'POST', 'DELETE'])
def organizations(request, pk=None):
    if request.method == 'GET' and pk is None:
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        organizations = Organization.objects.get(organization_id=pk)
        serializer = OrganizationSerializer(organizations, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        organization = Organization.objects.get(organization_id=pk)
        serializer = OrganizationSerializer(instance=organization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        organization = Organization.objects.get(organization_id=pk)
        organization.delete()
        return Response('Organization Successfully Deleted')


# Priority
@api_view(['GET', 'POST', 'DELETE'])
def priority(request, pk=None):
    if request.method == 'GET' and pk is None:
        priorities = Priority.objects.all()
        serializer = PrioritySerializer(priorities, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        priorities = Priority.objects.get(priority_id=pk)
        serializer = PrioritySerializer(priorities, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = PrioritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        priority = Priority.objects.get(priority_id=pk)
        serializer = PrioritySerializer(instance=priority, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        priority = Priority.objects.get(priority_id=pk)
        priority.delete()
        return Response('Priority Successfully Deleted')


# Subscription_Mode
@api_view(['GET', 'POST', 'DELETE'])
def subscriptionMode(request, pk=None):
    if request.method == 'GET' and pk is None:
        subscription_modes = SubscriptionMode.objects.all()
        serializer = SubscriptionModeSerializer(subscription_modes, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        subscription_modes = SubscriptionMode.objects.get(subscription_mode_id=pk)
        serializer = SubscriptionModeSerializer(subscription_modes, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = SubscriptionModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        subscription_mode = SubscriptionMode.objects.get(subscription_mode_id=pk)
        serializer = SubscriptionModeSerializer(instance=subscription_mode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        subscription_mode = SubscriptionMode.objects.get(subscription_mode_id=pk)
        subscription_mode.delete()
        return Response('Subscription Mode Successfully Deleted')


# User_Event_Subscription
@api_view(['GET', 'POST', 'DELETE'])
def userEventSubscription(request, pk=None):
    if request.method == 'GET' and pk is None:
        user_event_subscriptions = UserEventSubscription.objects.all()
        serializer = UserEventSubscriptionSerializer(user_event_subscriptions, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        user_event_subscriptions = UserEventSubscription.objects.get(user_event_subscription_id=pk)
        serializer = UserEventSubscriptionSerializer(user_event_subscriptions, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = UserEventSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        user_event_subscription = UserEventSubscription.objects.get(user_event_subscription_id=pk)
        serializer = UserEventSubscriptionSerializer(instance=user_event_subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        user_event_subscription = UserEventSubscription.objects.get(user_event_subscription_id=pk)
        user_event_subscription.delete()
        return Response('Priority Successfully Deleted')


# Venues
@api_view(['GET', 'POST', 'DELETE'])
def venues(request, pk=None):
    if request.method == 'GET' and pk is None:
        venues = Venues.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        venues = Venues.objects.get(venue_id=pk)
        serializer = VenueSerializer(venues, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        venue = Venues.objects.get(venue_id=pk)
        serializer = VenueSerializer(instance=venue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        venue = Venues.objects.get(venue_id=pk)
        venue.delete()
        return Response('Venue Successfully Deleted')


# Blood_Types
@api_view(['GET', 'POST', 'DELETE'])
def bloodTypes(request, pk=None):
    if request.method == 'GET' and pk is None:
        blood_types = BloodTypes.objects.all()
        serializer = BloodTypeSerializer(blood_types, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        blood_types = BloodTypes.objects.get(blood_type_id=pk)
        serializer = BloodTypeSerializer(blood_types, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = BloodTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        blood_type = BloodTypes.objects.get(blood_type_id=pk)
        serializer = BloodTypeSerializer(instance=blood_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        blood_type = BloodTypes.objects.get(blood_type_id=pk)
        blood_type.delete()
        return Response('Blood Type Successfully Deleted')


# Blood_Types_Compatibility
@api_view(['GET', 'POST', 'DELETE'])
def bloodTypeCompatibility(request, pk=None):
    if request.method == 'GET' and pk is None:
        items = BloodTypeCompatibility.objects.all()
        serializer = BloodTypeCompatibilitySerializer(items, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk:
        items = BloodTypeCompatibility.objects.get(blood_type_compatibility_id=pk)
        serializer = BloodTypeCompatibilitySerializer(items, many=False)
        return Response(serializer.data)

    if request.method == 'POST' and pk is None:
        serializer = BloodTypeCompatibilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'POST' and pk:
        item = BloodTypeCompatibility.objects.get(blood_type_compatibility_id=pk)
        serializer = BloodTypeCompatibilitySerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Not Valid')

    if request.method == 'DELETE' and pk:
        item = BloodTypeCompatibility.objects.get(blood_type_compatibility_id=pk)
        item.delete()
        return Response('Blood Type Compatibility Successfully Deleted')
