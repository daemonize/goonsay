from django.db import models

class VotedObjectsManager(models.Manager):
    def select_score(self):
        from django.contrib.contenttypes.models import ContentType
        model_type = ContentType.objects.get_for_model(self.model)
        table_name = self.model._meta.db_table
        return self.extra(select={'score': 'SELECT SUM(vote) FROM votes WHERE content_type_id=%i AND object_id=%s.id' % (int(model_type.id), table_name)})
