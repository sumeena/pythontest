from django.contrib.auth.models import User, AbstractUser
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


# class AddressBase(models.Model):
#     """ Base model for all addresses """
#     town = models.CharField('Town', max_length=150)
#     county = models.CharField('County', max_length=150)
#     postcode = models.CharField('Postcode', max_length=10)
#
#     class Meta:
#         abstract = True


# class GUser(AbstractUser):
#     """ Custom user model to handle user profile's data """
#
#
#     kind = models.IntegerField
#     gender = models.CharField('Gender')
#     middle_name = models.CharField('Middle Name(s)', max_length=150, blank=True)
#
#     @property
#     def surname(self):
#         return self.last_name


class AccountType(models.Model):
    number = models.IntegerField('Account type number', unique=True)
    name = models.CharField('Account type name', max_length=100)

    def __unicode__(self):
        return "{} {}".format(self.number, self.name)


class AbstractPerson(models.Model):
    """ Base class for all persons (applicants, additional users, etc.) """
    title = models.CharField('Title', max_length=100)
    gender = models.CharField('Gender', max_length=20)
    first_name = models.CharField('First name', max_length=100)
    middle_name = models.CharField('Middle name', max_length=100, blank=True)
    last_name = models.CharField('Surname', max_length=100)
    email = models.EmailField()

    class Meta:
        abstract = True


class AbstractBusiness(models.Model):

    registered_name = models.CharField('Business registered name', max_length=100)
    trading_name = models.CharField('Business trading name', max_length=100)
    registration_number = models.CharField('Business registration number', max_length=8)

    phone = models.CharField('Business phone', max_length=20)
    phone_ext = models.CharField('Business phone ext.', max_length=10)

    other_phone = models.CharField('Other phone', max_length=20, blank=True)
    other_phone_ext = models.CharField('Other phone ext.', max_length=10, blank=True)

    website = models.URLField('Website address', blank=True)

    email = models.EmailField()

    class Meta:
        abstract = True


class Applicant(AbstractPerson):
    """ Stores data for all applicant for the application """

    application = models.ForeignKey('Application', related_name='applicants')
    is_main = models.BooleanField(default=False)

    def __unicode__(self):
        return "Applicant {} {}".format(self.first_name, self.last_name)


class AbstractPartner(models.Model):
    PERSON = 1
    BUSINESS = 2
    PARTNER_TYPES = (
        (PERSON, 'Person'),
        (BUSINESS, 'Business')
    )

    partner_type = models.IntegerField('Partner type', choices=PARTNER_TYPES)

    class Meta:
        abstract = True


class PartnerPerson(AbstractPerson, AbstractPartner):
    application = models.ForeignKey('Application', related_name='partners_person')


class PartnerBusiness(AbstractBusiness, AbstractPartner):
    application = models.ForeignKey('Application', related_name='partners_business')


class Application(models.Model):

    account_type = models.ForeignKey('AccountType')
    created_dt = models.DateTimeField(auto_now_add=True)
    fixed_term = models.IntegerField('Fixed term')


class Address(models.Model):

    BUSINESS = 1
    PERSONAL = 2
    CORRESPONDENCE = 3

    ADDRESS_TYPES = (
        (BUSINESS, 'Business/Organisation address'),
        (PERSONAL, 'Personal address'),
        (CORRESPONDENCE, 'Correspondence address')
    )

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_objects = generic.GenericForeignKey('content_type', 'object_id')

    address_type = models.SmallIntegerField(choices=ADDRESS_TYPES)
    house_name = models.CharField('House/Building name', max_length=150, blank=True)
    house_number = models.CharField('House/Building number', max_length=50)
    street = models.CharField('Street name', max_length=150)
    town = models.CharField('Town', max_length=150)
    county = models.CharField('County', max_length=150)
    postcode = models.CharField('Postcode', max_length=10)
    date_moved = models.DateField('Date moved into this address')

    home_phone = models.CharField('Home telephone number', max_length=15, blank=True)
    mobile_phone = models.CharField('Mobile telephone number', max_length=15, blank=True)
    other_phone = models.CharField('Other telephone number', max_length=15, blank=True)
