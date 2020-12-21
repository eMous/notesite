from django.contrib import admin
from django.apps import apps
from django.contrib.auth.admin import UserAdmin

from .models.site_application import *
from .models.core import *
from django.contrib.admin.sites import AlreadyRegistered


# Auto register
def auto_register(model):
    # Get all fields from model, but exclude autocreated reverse relations
    field_list = [f.name for f in model._meta.get_fields() if f.auto_created == False]
    # Dynamically create ModelAdmin class and register it.
    my_admin = type('MyAdmin', (admin.ModelAdmin,),
                    {'list_display': field_list}
                    )
    try:
        admin.site.register(model, my_admin)
    except AlreadyRegistered:
        # This model is already registered
        pass


for model in apps.get_app_config('recorder').get_models():
    auto_register(model)


# Hack the customized user(which has the ManyToMany field: groups, permissions)
class UserProfileInline(admin.StackedInline):
    model = RecordedUser
    filter_horizontal = ()


class CustomUserAdmin(UserAdmin):
    filter_horizontal = ('user_permissions', 'groups')
    save_on_top = True
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login')


admin.site.unregister(RecordedUser)
admin.site.register(RecordedUser, CustomUserAdmin)
