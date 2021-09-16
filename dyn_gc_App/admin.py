from django.contrib import admin
from dyn_gc_App.models import User, Master, Plot


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "first_name", "last_name", "mobile", "email", "dob"]


class MasterAdmin(admin.ModelAdmin):
    list_display = ["thumbnails"]


class PlotAdmin(admin.ModelAdmin):
    list_display = ["plot_num", "plot_size", "status"]


admin.site.register(User, UserAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Plot, PlotAdmin)