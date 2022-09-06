from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import User


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
	    (None, { 
            'fields': (
                'email',  'username', 'first_name', 'last_name', 'password1', ),
            }
        ),
    )

admin.site.register(User, CustomUserAdmin)

