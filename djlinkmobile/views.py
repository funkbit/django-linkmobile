import logging

from django.http import HttpResponse

from djlinkmobile.models import AckMessage


logger = logging.getLogger(__name__)

def callback(request):
    """
    Link Mobile will send an ack forward callback (as HTTP Get) to us.
    
    Doc:
    http://msgw.linkmobility.com/MessageService.htm#AckForward
    """
    
    logger.debug('Got callback from Link Mobile: %(raw_get_data)s\n%(meta)s' % {
        'raw_get_data': request.GET,
        'meta': request.META,
    })
    
    try:
        ack = AckMessage()
        ack.batchid = request.GET.get('BatchID', '')
        ack.msisdn = request.GET.get('Msisdn', '')
        ack.price = request.GET.get('Price', '')
        ack.operator = request.GET.get('Operator', '')
        ack.messageid = request.GET.get('MessageID', '')
        ack.parts = request.GET.get('Parts', '')
        ack.statuscode = request.GET.get('StatusCode', '')
        ack.substatuscodes = request.GET.get('SubStatusCodes', '')
        ack.save()
    except:
        logger.exception('Could not save link mobile ACK message with BatchID %(batchid)s, MessageID %(msgid)s. Returning NOK.' % {
            'batchid': request.GET.get('BatchID', ''),
            'msgid': request.GET.get('MessageID', '')
        })
        return HttpResponse('NOK', content_type='text/plain')
    
    return HttpResponse('OK', content_type='text/plain')
