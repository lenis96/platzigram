from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','user','phone_number','website','picture')
    list_display_links=('pk','user')
    list_editable=('phone_number','website','picture')

    search_fields=(
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
    )
    list_filter=(
        'created',
        'modified'
    )

    fieldsets=(
        ('Porfile',{
            'fields':(('user','picture'),),
        }),
        ('Extra Info',{
            'fields':(
                ('website','phone_number'),
                ('biography'),),
        }),
        ('Metadta',{
            'fields':(
                ('created','modified'),
            )
        })
    )
    readonly_fields=('created','modified')

class ProfileInline(admin.StackedInline):
    model=Profile
    can_delete=False
    verbose_name_plural='profiles'

class UserAdmin(BaseUserAdmin):
    inlines=(ProfileInline,)
    list_display=(
        'username',
        'email',
        'first_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)