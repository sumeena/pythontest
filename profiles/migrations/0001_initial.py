# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AccountType'
        db.create_table('profiles_accounttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('profiles', ['AccountType'])

        # Adding model 'Applicant'
        db.create_table('profiles_applicant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='applicants', to=orm['profiles.Application'])),
            ('is_main', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('profiles', ['Applicant'])

        # Adding model 'PartnerPerson'
        db.create_table('profiles_partnerperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('partner_type', self.gf('django.db.models.fields.IntegerField')()),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partners_person', to=orm['profiles.Application'])),
        ))
        db.send_create_signal('profiles', ['PartnerPerson'])

        # Adding model 'PartnerBusiness'
        db.create_table('profiles_partnerbusiness', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registered_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('trading_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('registration_number', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone_ext', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('other_phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('other_phone_ext', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('partner_type', self.gf('django.db.models.fields.IntegerField')()),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='partners_business', to=orm['profiles.Application'])),
        ))
        db.send_create_signal('profiles', ['PartnerBusiness'])

        # Adding model 'Application'
        db.create_table('profiles_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.AccountType'])),
            ('created_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('fixed_term', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('profiles', ['Application'])

        # Adding model 'Address'
        db.create_table('profiles_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('address_type', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('house_name', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('house_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('town', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date_moved', self.gf('django.db.models.fields.DateField')()),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('other_phone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
        ))
        db.send_create_signal('profiles', ['Address'])


    def backwards(self, orm):
        # Deleting model 'AccountType'
        db.delete_table('profiles_accounttype')

        # Deleting model 'Applicant'
        db.delete_table('profiles_applicant')

        # Deleting model 'PartnerPerson'
        db.delete_table('profiles_partnerperson')

        # Deleting model 'PartnerBusiness'
        db.delete_table('profiles_partnerbusiness')

        # Deleting model 'Application'
        db.delete_table('profiles_application')

        # Deleting model 'Address'
        db.delete_table('profiles_address')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.accounttype': {
            'Meta': {'object_name': 'AccountType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        'profiles.address': {
            'Meta': {'object_name': 'Address'},
            'address_type': ('django.db.models.fields.SmallIntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'date_moved': ('django.db.models.fields.DateField', [], {}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'house_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'house_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'other_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'profiles.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applicants'", 'to': "orm['profiles.Application']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.application': {
            'Meta': {'object_name': 'Application'},
            'account_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.AccountType']"}),
            'created_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fixed_term': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'profiles.partnerbusiness': {
            'Meta': {'object_name': 'PartnerBusiness'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partners_business'", 'to': "orm['profiles.Application']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'other_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'other_phone_ext': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'partner_type': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone_ext': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registered_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'trading_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'profiles.partnerperson': {
            'Meta': {'object_name': 'PartnerPerson'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partners_person'", 'to': "orm['profiles.Application']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'partner_type': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['profiles']