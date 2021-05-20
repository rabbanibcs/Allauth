from django.contrib import admin
from .models import News, Games, Ladders, userdtl, Banner, sliders, Social, image, team, Contact, Setting


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','desc', 'update_at','status']
    readonly_fields = ('name', 'email', 'phone', 'desc', 'ip')
    list_filter = ['status']

class SettingAdmin(admin.ModelAdmin):
    list_display = ['aboutus','contact', 'update_at','status']

admin.site.register(userdtl)
admin.site.register(News)
admin.site.register(Games)
admin.site.register(Ladders)
admin.site.register(Banner)
admin.site.register(sliders)
admin.site.register(Social)
admin.site.register(image)
admin.site.register(team)
# admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Setting,SettingAdmin)
