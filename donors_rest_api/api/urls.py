from django.urls import path
from  . import views

from . import views

urlpatterns = [
    path('', views.apiRoot, name='Api-Root'),

    path('users/', views.users, name='Users'),
    path('users/<int:pk>', views.users, name='Users'),

    path('districs/', views.districts, name='Districts'),
    path('districs/<int:pk>', views.districts, name='Districts'),

    path('cities/', views.cities, name='Cities'),
    path('cities/<int:pk>', views.cities, name='Cities'),

    path('donation_history/', views.donationHistory, name='Donation-History'),
    path('donation_history/<int:pk>', views.donationHistory, name='Donation-History'),

    path('donation_modes/', views.donationModes, name='Donation-Modes'),
    path('donation_modes/<int:pk>', views.donationModes, name='Donation-Modes'),

    path('donation_regs/', views.donationReg, name='Donation-Regs'),
    path('donation_regs/<int:pk>', views.donationReg, name='Donation-Regs'),

    path('donation_reqs/', views.donationRequests, name='Donation-Reqs'),
    path('donation_reqs/<int:pk>', views.donationRequests, name='Donation-Reqs'),

    path('donations/', views.donations, name='Donations'),
    path('donations/<int:pk>', views.donations, name='Donations'),

    path('donations_donation_modes/', views.donationsDonationModes, name='Donations-Donation-Modes'),
    path('donations_donation_modes/<int:pk>', views.donationsDonationModes, name='Donations-Donation-Modes'),

    path('events/', views.events, name='Events'),
    path('events/<int:pk>', views.events, name='Events'),

    path('event_types/', views.eventType, name='Event-Types'),
    path('event_types/<int:pk>', views.eventType, name='Event-Types'),

    path('organizations/', views.organizations, name='Organizations'),
    path('organizations/<int:pk>', views.organizations, name='Organizations'),

    path('priorities/', views.priority, name='Priorities'),
    path('priorities/<int:pk>', views.priority, name='Priorities'),

    path('subscription_modes/', views.subscriptionMode, name='Subscription-Modes'),
    path('subscription_modes/<int:pk>', views.subscriptionMode, name='Subscription-Modes'),

    path('user_event_subscription/', views.userEventSubscription, name='User-Event-Subscription'),
    path('user_event_subscription/<int:pk>', views.userEventSubscription, name='User-Event-Subscription'),

    path('venues/', views.venues, name='Venues'),
    path('venues/<int:pk>', views.venues, name='Venues'),

    path('blood_types/', views.bloodTypes, name='Blood Types'),
    path('blood_types/<int:pk>', views.bloodTypes, name='Blood Types'),

    path('blood_type_compatibility/', views.bloodTypeCompatibility, name='Blood-Type-Compatibility'),
    path('blood_type_compatibility/<int:pk>', views.bloodTypeCompatibility, name='Blood-Type-Compatibility'),
]