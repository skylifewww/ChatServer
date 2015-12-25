from django.contrib import admin
from models import Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['sent_by',
                    'sent_at',
                    'received_at',
                    'received_by']

    list_filter = ['is_viewed']

    def sent_by(self, obj):
        return obj.sent_by.username

    def received_by(self, obj):
        return obj.received_by.username

admin.site.register(Message, MessageAdmin)
