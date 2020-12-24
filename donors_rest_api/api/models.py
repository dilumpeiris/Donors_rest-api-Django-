from django.db import models


class BloodTypeCompatibility(models.Model):
    blood_type_compatibility_id = models.AutoField(primary_key=True)
    donor_blood_type = models.OneToOneField('BloodTypes', models.DO_NOTHING, db_column='donor_blood_type')
    recv_blood_type = models.ForeignKey('BloodTypes', models.DO_NOTHING, db_column='recv_blood_type', related_name='+')
    is_compatible = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.donor_blood_type)+ " - " + str(self.recv_blood_type)

    class Meta:
        managed = False
        db_table = 'blood_type_compatibility'
        unique_together = (('donor_blood_type', 'recv_blood_type'),)


class BloodTypes(models.Model):
    blood_type_id = models.AutoField(primary_key=True)
    blood_type = models.CharField(max_length=5)

    def __str__(self):
        return self.blood_type

    class Meta:
        managed = False
        db_table = 'blood_types'


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    district = models.ForeignKey('Districts', models.DO_NOTHING)

    def __str__(self):
        return self.city_name

    class Meta:
        managed = False
        db_table = 'cities'


class Districts(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.district_name

    class Meta:
        managed = False
        db_table = 'districts'


class DonationHistory(models.Model):
    donation_history_item_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    donation = models.ForeignKey('Donations', models.DO_NOTHING)
    venue = models.ForeignKey('Venues', models.DO_NOTHING)
    donation_date = models.DateField()
    donation_timestamp = models.DateTimeField()
    verification_user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True, related_name='users')

    def __str__(self):
        return str(self.user)+": "+str(self.donation_date)

    class Meta:
        managed = False
        db_table = 'donation_history'
        unique_together = (('user', 'donation', 'venue', 'donation_date'),)


class DonationModes(models.Model):
    donation_mode_id = models.AutoField(primary_key=True)
    donation_mode = models.CharField(max_length=45)
    donation_freq = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.donation_mode

    class Meta:
        managed = False
        db_table = 'donation_modes'


class DonationReg(models.Model):
    donation_reg_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    donation = models.ForeignKey('Donations', models.DO_NOTHING)
    last_donation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.user) +" - "+ str(self.donation)

    class Meta:
        managed = False
        db_table = 'donation_reg'
        unique_together = (('user', 'donation'),)


class Donations(models.Model):
    donation_id = models.AutoField(primary_key=True)
    donation_type = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.donation_type

    class Meta:
        managed = False
        db_table = 'donations'


class DonationsDonationModes(models.Model):
    donations_donation_modes_id = models.AutoField(primary_key=True)
    donation = models.OneToOneField(Donations, models.DO_NOTHING)
    donation_mode = models.ForeignKey(DonationModes, models.DO_NOTHING)

    def __str__(self):
        return str(self.donation) + " - "+ str(self.donation_mode)

    class Meta:
        managed = False
        db_table = 'donations_donation_modes'
        unique_together = (('donation', 'donation_mode'),)


class EventType(models.Model):
    event_type_id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=50)

    def __str__(self):
        return self.event_type

    class Meta:
        managed = False
        db_table = 'event_type'


class Events(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    event_name = models.CharField(max_length=50)
    event_type = models.ForeignKey(EventType, models.DO_NOTHING)
    event_start_date = models.DateField(blank=True, null=True)
    event_end_date = models.DateField(blank=True, null=True)
    event_start_time = models.TimeField(blank=True, null=True)
    event_end_time = models.TimeField(blank=True, null=True)
    event_desc = models.CharField(max_length=1000, blank=True, null=True)
    city = models.ForeignKey(Cities, models.DO_NOTHING)
    organization = models.ForeignKey('Organization', models.DO_NOTHING)

    def __str__(self):
        return self.event_name

    class Meta:
        managed = False
        db_table = 'events'


class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=50)
    organization_desc = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.organization_name

    class Meta:
        managed = False
        db_table = 'organization'


class Priority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority_name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.priority_name

    class Meta:
        managed = False
        db_table = 'priority'




class Requests(models.Model):
    request_id = models.BigAutoField(primary_key=True)
    request_title = models.CharField(max_length=50, blank=True, null=True)
    donation = models.ForeignKey(Donations, models.DO_NOTHING)
    blood_type = models.ForeignKey(BloodTypes, models.DO_NOTHING)
    request_start_date = models.DateField(blank=True, null=True)
    request_end_date = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    priority_priority = models.ForeignKey(Priority, models.DO_NOTHING)

    def __str__(self):
        return self.request_title

    class Meta:
        managed = False
        db_table = 'requests'


class SubscriptionMode(models.Model):
    subscription_mode_id = models.AutoField(primary_key=True)
    subscription_mode = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.subscription_mode

    class Meta:
        managed = False
        db_table = 'subscription_mode'


class UserEventSubscription(models.Model):

    user_event_subscription_id = models.AutoField(primary_key=True)
    user = models.OneToOneField('Users', models.DO_NOTHING)
    event_type = models.ForeignKey(EventType, models.DO_NOTHING)
    subscription_mode = models.ForeignKey(SubscriptionMode, models.DO_NOTHING)

    def __str__(self):
        return str(self.user) +" - "+ str(self.event_type) + str(f"({self.subscription_mode})")

    class Meta:
        managed = False
        db_table = 'user_event_subscription'
        unique_together = (('user', 'event_type', 'subscription_mode'),)


class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    display_name = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    city = models.ForeignKey(Cities, models.DO_NOTHING, blank=True, null=True)
    blood_type = models.ForeignKey(BloodTypes, models.DO_NOTHING, db_column='blood_type', blank=True, null=True)
    reputation = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'users'


class Venues(models.Model):
    venue_id = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=50)
    venue_address = models.CharField(max_length=100, blank=True, null=True)
    venue_lat_lon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.venue_name

    class Meta:
        managed = False
        db_table = 'venues'
