from django.contrib import admin

from djlinkmobile.models import AckMessage


class AckMessageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'msisdn', 'messageid', 'statuscode')
    list_filter = ('created', )
    search_fields = ('id', 'msisdn', 'messageid')
    readonly_fields = AckMessage._meta.get_all_field_names()

admin.site.register(AckMessage, AckMessageAdmin)
