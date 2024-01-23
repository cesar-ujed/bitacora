from django.contrib import admin
from api.models import *


# # Profile detallado

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_group')
    search_fields = ('user_username', 'usergroups_name')
    list_filter = ('user__groups',)

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Departamento)
admin.site.register(Planeacion)
admin.site.register(Servicios)
admin.site.register(Internacionalizacion)
admin.site.register(Desarrollo)