from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('name', 'email', 'text', 'created_at')
    readonly_fields = list_display
    ordering = ('-created_at',)

    def queryset(self, request):
        qs = super(MessageAdmin, self).queryset(request)
        return qs.filter(question__isnull=True)

admin.site.register(Message, MessageAdmin)
