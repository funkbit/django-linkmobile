from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AckMessage(models.Model):
    """
    An ack forward message received by the Link Mobile API.
    """
    
    batchid = models.CharField(_('BatchID'), max_length=100, blank=True)
    msisdn = models.CharField(_('Msisdn'), max_length=100, blank=True)
    operator = models.CharField(_('Operator'), max_length=100, blank=True)
    messageid = models.CharField(_('MessageID'), max_length=100, blank=True)
    parts = models.CharField(_('Parts'), max_length=100, blank=True)
    statuscode = models.CharField(_('StatusCode'), max_length=100, blank=True)
    substatuscodes = models.CharField(_('SubStatusCodes'), max_length=100, blank=True)
    
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    
    def __unicode__(self):
        return _('AckMessage %s') % self.id
    
    class Meta:
        verbose_name = _('ack message')
        verbose_name_plural = _('ack messages')
