from django.contrib import admin
from project.models import Reservation, User, Menu
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'people', 'time', 'phone',
                    'date_reserved', 'status']


class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('picture',)}),
    )

class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','picture',
                    'description', 'type', 'category','location']
admin.site.register(User, MyUserAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Menu, MenuAdmin)
