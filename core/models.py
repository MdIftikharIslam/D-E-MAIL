import uuid

from django.db import models

class SendMail(models.Model):
    uid = models.UUIDField(default=uuid.uuid4(), editable=False)
    to = models.EmailField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        unique_id = str(self.uid)
        return unique_id

