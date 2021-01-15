# Donors REST API Django
Donors_rest_api-Django


<h2>API endpoints</h2>


<table>
    <tr>
        <th>endpoint</th>
        <th>description</th>
    </tr>
    <tr>
        <td>/login</td>
        <td>login user with valid credentials:Returns an access token</td>
    </tr>
    <tr>
        <td>/user_create</td>
        <td>create a new user</td>
    </tr>
    <tr>
        <td>/users</td>
        <td>view all the current users</td>
    </tr>
    <tr>
        <td>/users/&lt;int:pk&gt;/</td>
        <td>view a particular user, update/delete user</td>
    </tr>
        <tr>
        <td>/cities</td>
        <td>view all the current cities</td>
    </tr>
    <tr>
        <td>/cities/&lt;int:pk&gt;/</td>
        <td>view a particular city, create a new city, update/delete city</td>
    </tr>
        </tr>
        <tr>
        <td>/districts</td>
        <td>view all the current districts</td>
    </tr>
    <tr>
        <td>/districts/&lt;int:pk&gt;/</td>
        <td>view a particular district, create a new district, update/delete district</td>
    </tr>
            </tr>
        <tr>
        <td>/donations</td>
        <td>view all the current donations</td>
    </tr>
    <tr>
        <td>/donations/&lt;int:pk&gt;/</td>
        <td>view a particular donation, create a new donation, update/delete donation</td>
    </tr>
        </tr>
        <tr>
        <td>/donation_history</td>
        <td>view all donation history items</td>
    </tr>
    <tr>
        <td>/donation_history/&lt;int:pk&gt;/</td>
        <td>view a particular donation history item, create a new item, update/delete item</td>
    </tr>
        </tr>
        <tr>
        <td>/donation_modes</td>
        <td>view all donation modes</td>
    </tr>
    <tr>
        <td>/donation_modes/&lt;int:pk&gt;/</td>
        <td>view a particular donation mode, create a new donation mode, update/delete donation mode</td>
    </tr>
        </tr>
        <tr>
        <td>/donation_regs</td>
        <td>view all donation reg items</td>
    </tr>
    <tr>
        <td>/donation_regs/&lt;int:pk&gt;/</td>
        <td>view a particular donation reg item, create a new donation reg item, update/delete donation reg item</td>
    </tr>
        </tr>
        <tr>
        <td>/donations_donation_modes</td>
        <td>view all donations donation mode items</td>
    </tr>
    <tr>
        <td>/donations_donation_modes/&lt;int:pk&gt;/</td>
        <td>view a particular donations donation mode item, create a item, update/delete item</td>
    </tr>
        </tr>
        <tr>
        <td>/events</td>
        <td>view all the current events</td>
    </tr>
    <tr>
        <td>/events/&lt;int:pk&gt;/</td>
        <td>view a particular event, create a new event, update/delete event</td>
    </tr>
        </tr>
        <tr>
        <td>/event_types</td>
        <td>view all event types</td>
    </tr>
    <tr>
        <td>/event_types/&lt;int:pk&gt;/</td>
        <td>view a particular event type, create a new event type, update/delete event type</td>
    </tr>
        </tr>
        <tr>
        <td>/organizations</td>
        <td>view all the current organizations</td>
    </tr>
    <tr>
        <td>/organizations/&lt;int:pk&gt;/</td>
        <td>view a particular organization, create a new organization, update/delete organization</td>
    </tr>
        </tr>
        <tr>
        <td>/priorities</td>
        <td>view all the current priorities</td>
    </tr>
    <tr>
        <td>/priorities/&lt;int:pk&gt;/</td>
        <td>view a particular priority, create a new priority, update/delete priority</td>
    </tr>
        </tr>
        <tr>
        <td>/subscription_modes</td>
        <td>view all subscription modes</td>
    </tr>
    <tr>
        <td>/subscription_modes/&lt;int:pk&gt;/</td>
        <td>view a particular subscription mode, create a new subscription mode, update/delete subscription mode</td>
    </tr>
        </tr>
        <tr>
        <td>/user_event_subscriptions</td>
        <td>view all user-event-subscription items</td>
    </tr>
    <tr>
        <td>/user_event_subscriptions/&lt;int:pk&gt;/</td>
        <td>view a particular user-event-subscription item, create a new item, update/delete item</td>
    </tr>
        </tr>
        <tr>
        <td>/venues</td>
        <td>view all the current venues</td>
    </tr>
    <tr>
        <td>/venues/&lt;int:pk&gt;/</td>
        <td>view a particular venue, create a new venue, update/delete venue</td>
    </tr>
        </tr>
        <tr>
        <td>/blood_types</td>
        <td>view all blood types</td>
    </tr>
    <tr>
        <td>/blood_types/&lt;int:pk&gt;/</td>
        <td>view a particular blood type, create a new blood tyepe, update/delete blood type</td>
    </tr>
        </tr>
        <tr>
        <td>/blood_type_compatibility</td>
        <td>view all blood-type-compatibility items</td>
    </tr>
    <tr>
        <td>/blood_type_compatibility/&lt;int:pk&gt;/</td>
        <td>view a particular blood-type-compatibility item, create a new item, update/delete item</td>
    </tr>

</table>

# JSON POST Queries

## Users
```JSON
{
    "username": "username",
    "password": "password",
    "email": "email",
    "display_name": "display_name",
    "create_time": "create_time",
    "city": "city",
    "blood_type": "blood_type",
    "reputation": "reputation",
    "remember_token": "remember_token",
}
```
## Cities
```JSON
{
    "city_name": "city_name",
    "district": "district",
}
```
## Districts
```JSON
{
    "district_name": "district_name",
}
```
## Blood Types
```JSON
{
    "blood_type": "blood_type",
}
```
## Blood Type Compatibility
```JSON
{
    "donor_blood_type": "donor_blood_type",
    "recv_blood_type": "recv_blood_type",
    "is_compatible": "is_compatible",
}
```

## Donation History
```JSON
{
    "user": "user",
    "donation": "donation",
    "venue": "venue",
    "donation_date": "donation_date",
    "donation_timestamp": "donation_timestamp",
    "verification_user": "verification_user",
}
```

## Donation Modes
```JSON
{
    "donation_mode": "donation_mode",
    "donation_freq": "donation_freq",
}
```
## Donation Regs
```JSON
{
    "user": "user",
    "donation": "donation",
    "last_donation_date": "last_donation_date",
}
```

## Donations
```JSON
{
    "donation_type": "donation_type",
}
```

## Donations Donation Modes
```JSON
{
    "donation": "donation",
    "donation_mode": "donation_mode",
}
```

## EventType
```JSON
{
    "event_type": "event_type",
}
```

## Events
```JSON
{
    "event_name": "event_name",
    "event_type": "event_type",
    "event_start_date": "event_start_date",
    "event_end_date": "event_end_date",
    "event_start_time": "event_start_time",
    "event_end_time": "event_end_time",
    "event_desc": "event_desc",
    "city": "city",
    "organization": "organization",
}
```

## Organizations
```JSON
{
    "organization_name": "organization_name",
    "organization_desc": "organization_desc",
}
```

## Priorities
```JSON
{
    "priority_name": "priority_name",
}
```

## Requests
```JSON
{
    "request_title": "request_title",
    "donation": "donation",
    "blood_type": "blood_type",
    "request_start_date": "request_start_date",
    "request_end_date": "request_end_date",
    "timestamp": "timestamp",
    "priority_priority": "priority_priority",
}
```

## Subscription Modes
```JSON
{
    "subscription_mode": "subscription_mode",
}
```

## User Event Subscriptions
```JSON
{
    "user": "user",
    "event_type": "event_type",
    "subscription_mode": "subscription_mode",
}
```

## Venues
```JSON
{
    "venue_name": "venue_name",
    "venue_address": "venue_address",
    "venue_lat_lon": "venue_lat_lon",
}
```
