
from south.db import db
from django.db import models
from goonsay.apps.goonsay.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'GoonSay'
        db.create_table('goonsay_goonsay', (
            ('id', orm['goonsay.GoonSay:id']),
            ('text', orm['goonsay.GoonSay:text']),
            ('added', orm['goonsay.GoonSay:added']),
            ('added_ip', orm['goonsay.GoonSay:added_ip']),
        ))
        db.send_create_signal('goonsay', ['GoonSay'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'GoonSay'
        db.delete_table('goonsay_goonsay')
        
    
    
    models = {
        'goonsay.goonsay': {
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'added_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }
    
    complete_apps = ['goonsay']
