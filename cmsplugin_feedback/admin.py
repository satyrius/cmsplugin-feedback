from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('name', 'email', 'text', 'created_at')
    readonly_fields = list_display
    ordering = ('-created_at',)

admin.site.register(Message, MessageAdmin)
