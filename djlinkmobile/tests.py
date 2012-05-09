import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

from djlinkmobile.models import AckMessage

class AckMessageTests(TestCase):
    
    def testCallbackView(self):
        """
        Test callback view with an ack message.
        """
        
        url = reverse('djlinkmobile-callback') + '?BatchID=test1&Msisdn=%2B4798765432&Operator=no.tele2&MessageID=1&Parts=2&StatusCode=1&SubStatusCodes=6,6'
        response = self.client.get(url)
        
        # Check the response
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'OK')
        
        # Check the new object
        self.assertEquals(AckMessage.objects.count(), 1)
        
        # Check that fields are set correctly
        obj = AckMessage.objects.get()
        self.assertEquals(obj.batchid, 'test1')
        self.assertEquals(obj.msisdn, '+4798765432')
        
        self.assertTrue(isinstance(obj.created, datetime.datetime))
        self.assertTrue(isinstance(obj.modified, datetime.datetime))
