from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from petstagram.account.models import PetstagramUser

UserModel = get_user_model()


@admin.register(UserModel)
class PetstagramUserAdmin(UserAdmin):
    list_display = (
        'email',
        'is_staff',
    )
    search_fields = (
        'email',
        'username',
    )
    readonly_fields = (
        'date_joined',
    )
    ordering = (
        'email',
    )
    list_filter = (
        'groups',
        'is_staff',
        'is_superuser',
    )
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )}),
        ('Important dates', {
            'fields': (
                'date_joined',
                'last_login',
            )}),
        ('Permissions', {
            'fields': (
                'groups',
                'user_permissions',
                'is_staff',
                'is_superuser',
            )}),
    )
    add_fieldsets = (
        ('User credentials', {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2'
            ),
        }),
    )
