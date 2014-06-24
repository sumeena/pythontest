import json
import pprint
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.http import HttpResponse
from django.views.generic import View


class ApplicationForm(forms.Form):
    account_type = forms.IntegerField()
    fixed_term = forms.IntegerField()
    password = forms.CharField()
    confirm_password = forms.CharField()
    pin = forms.RegexField('[0-9]+', max_length=4, min_length=4)
    security_question = forms.CharField(min_length=5)
    security_answer = forms.CharField(min_length=6)
    security_answer_confirm = forms.CharField(min_length=6)

    def clean(self):
        cd = super(ApplicationForm, self).clean()
        sa = cd.get('security_answer')
        sac = cd.get('security_answer_confirm')
        #if sa != sac:
        #   raise ValidationError('Security answer and confirmation must be equal.')
        return cd

            # 'nominated_account': {
            #     'bank_name': 'Citibank',
            #     'sort_code': '11-23-60',
            #     'account_number': '12341234',
            #     'roll_number': '',
            #     'account_holders': [{
            #         'name': 'John M. Doe',
            #     }],
            #     'time_since': "5/3",
            # },

class NominatedAccountForm(forms.Form):
    bank_name = forms.CharField()
    sort_code = forms.RegexField('[0-9]+', max_length=6, min_length=6)
    account_number = forms.CharField()
    roll_number = forms.CharField(required=False)
    #account_holders =

class Register(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode(encoding='UTF-8'))
        application_form = ApplicationForm(data)
        print(application_form.is_valid(), application_form.errors)
        if application_form.is_valid():
            nominated_account = data.get('nominated_account')
        return HttpResponse()
