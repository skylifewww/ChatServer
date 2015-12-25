from django.contrib import admin

from models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_seen_at']
    
admin.site.register(UserProfile, UserProfileAdmin)