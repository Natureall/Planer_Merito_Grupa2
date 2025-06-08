from django.contrib import admin
from .models import Ocena

admin.site.register(Ocena)

from .models import AdminMessage

@admin.register(AdminMessage)
class AdminMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created_at')
    list_filter = ('active',)
    search_fields = ('title', 'content')
