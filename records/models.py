from django.db import models

from django.db import models

class Record(models.Model):
    index = models.AutoField(primary_key=True)
    input_data = models.JSONField()
    output_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'record'  # Explicitly set the table name