import datetime
import json
from django.test import Client
from unittest import TestCase
from profiles.models import Application, AccountType, Applicant


class ESaverRegistrationCase(TestCase):

    def setUp(self):
        account_type = AccountType.objects.create(number=1, name='e-Saver')
        self.account_type = account_type
        self.c = Client()

    def tearDown(self):
        pass

    def test_application(self):
        data = {
            'account_type': 1,
            'fixed_term': 1,
            'password': 'password',
            'confirm_password': 'password',
            'pin': '1244',
            'security_question': 'My first mobile?',
            'security_answer': 'Nokia 3110',
            'security_answer_confirm': 'Nokia 3110',
            'applicants': [{
                'id': 1,
                'is_main': True,
                'title': 'Mr.',
                'gender': 'male',
                'first_name': 'John',
                'middle_name': 'Martin',
                'last_name': 'Doe',
                'date_of_birth': str(datetime.date(1988, 2, 11)),
                'nationality': 'Russian',
                'occupation': 'Specialist',
                'email': 'john@example.com',
                'confirm_email': 'john@example.com',
                'addresses': [{
                    'is_current': True,
                    'house_name': '',
                    'house_number': '1234',
                    'street': 'Main st.',
                    'town': 'London',
                    'county': 'County',
                    'postcode': '10002',
                    'date_moved_in': str(datetime.date(2010, 2, 11)),
                    'home_phone': '',
                    'mobile_phone': '+79125150101',
                    'other_phone': '',
                },]
            }],
            'nominated_account': {
                'bank_name': 'Citibank',
                'sort_code': '11-23-60',
                'account_number': '12341234',
                'roll_number': '',
                'account_holders': [{
                    'name': 'John M. Doe',
                }],
                'time_since': "5/3",
            },

        }
        data = json.dumps(data)
        print(data)
        r = self.c.post('/profiles/register/', data, content_type='application/json')
