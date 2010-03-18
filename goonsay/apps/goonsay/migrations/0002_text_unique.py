
from south.db import db
from django.db import models
from goonsay.apps.goonsay.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Creating unique_together for [text] on GoonSay.
        db.create_unique('goonsay_goonsay', ['text'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [text] on GoonSay.
        db.delete_unique('goonsay_goonsay', ['text'])
        
    
    
    models = {
        'goonsay.goonsay': {
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'added_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        }
    }
    
    complete_apps = ['goonsay']
