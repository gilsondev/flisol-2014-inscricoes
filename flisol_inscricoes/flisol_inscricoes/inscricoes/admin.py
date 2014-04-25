from django.contrib import admin

from .models import Interesse, Oficina, Participante


class InteresseAdmin(admin.ModelAdmin):
    pass


class ParticipanteAdmin(admin.ModelAdmin):
    pass


class OficinaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Interesse, InteresseAdmin)
admin.site.register(Oficina, OficinaAdmin)
admin.site.register(Participante, ParticipanteAdmin)
