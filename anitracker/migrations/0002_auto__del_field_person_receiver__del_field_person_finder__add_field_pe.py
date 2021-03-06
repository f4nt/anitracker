# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Person.receiver'
        db.delete_column('anitracker_person', 'receiver')

        # Deleting field 'Person.finder'
        db.delete_column('anitracker_person', 'finder')

        # Adding field 'Person.person_type'
        db.add_column('anitracker_person', 'person_type', self.gf('django.db.models.fields.CharField')(default='finder', max_length=16), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Person.receiver'
        db.add_column('anitracker_person', 'receiver', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Person.finder'
        db.add_column('anitracker_person', 'finder', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Person.person_type'
        db.delete_column('anitracker_person', 'person_type')


    models = {
        'anitracker.admission': {
            'Meta': {'object_name': 'Admission'},
            'animal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.Animal']"}),
            'animal_age': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_admission': ('django.db.models.fields.DateField', [], {}),
            'disposition': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'disposition_date': ('django.db.models.fields.DateField', [], {}),
            'follow_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'received_from': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'received_person'", 'null': 'True', 'to': "orm['anitracker.Person']"}),
            'released_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anitracker.Person']", 'null': 'True', 'blank': 'True'})
        },
        'anitracker.animal': {
            'Meta': {'object_name': 'Animal'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'sub_type': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'anitracker.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'address_two': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'telephone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['anitracker']
