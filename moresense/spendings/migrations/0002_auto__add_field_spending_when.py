# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration

class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Spending.when'
        db.add_column('spendings_spending', 'when',
            self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 1, 4, 9, 14, 54, 663002)),
            keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Spending.when'
        db.delete_column('spendings_spending', 'when')


    models = {
        'spendings.household': {
            'Meta': {'object_name': 'Household'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'spendings.person': {
            'Meta': {'object_name': 'Person'},
            'household': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['spendings.Household']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'default': "'46e257f3'", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'spendings.spending': {
            'Meta': {'object_name': 'Spending'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['spendings.Person']"}),
            'when': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['spendings']
