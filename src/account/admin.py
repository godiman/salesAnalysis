from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


# custom admin
class AdminAccount(UserAdmin):
    list_display = ('email', 'first_name', 'last_name','date_joined', 'last_login', 'is_admin', 'is_staff', )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
# Register your models here.
admin.site.register(Account, AdminAccount)