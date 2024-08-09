from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

# admin.site.register(CustomUser)

admin.site.register(Content)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(TeamMember)
admin.site.register(Career)
admin.site.register(Image)
admin.site.register(Category)


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )