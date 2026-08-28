from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, verbose_name=_('recipient'))
    subject = models.TextField(verbose_name=_('subject'))
    body = models.TextField(verbose_name=_('body'))
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
