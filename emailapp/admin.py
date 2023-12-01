from django.contrib import admin
from .models import Email


class EmailAdmin(admin.ModelAdmin):
    # Customize the displayed fields
    list_display = ('subject', 'recipient', 'sent_at')


admin.site.register(Email, EmailAdmin)
