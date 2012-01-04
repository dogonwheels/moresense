# encoding: utf-8
from south.db import db
from south.v2 import SchemaMigration

class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Household'
        db.create_table('spendings_household', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ))
        db.send_create_signal('spendings', ['Household'])

        # Adding model 'Person'
        db.create_table('spendings_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('household', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spendings.Household'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('identifier', self.gf('django.db.models.fields.CharField')(default='ee58092a', max_length=50)),
            ))
        db.send_create_signal('spendings', ['Person'])

        # Adding model 'Spending'
        db.create_table('spendings_spending', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spendings.Person'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ))
        db.send_create_signal('spendings', ['Spending'])


    def backwards(self, orm):
        # Deleting model 'Household'
        db.delete_table('spendings_household')

        # Deleting model 'Person'
        db.delete_table('spendings_person')

        # Deleting model 'Spending'
        db.delete_table('spendings_spending')


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
            'identifier': ('django.db.models.fields.CharField', [], {'default': "'04144deb'", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'spendings.spending': {
            'Meta': {'object_name': 'Spending'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['spendings.Person']"})
        }
    }

    complete_apps = ['spendings']
