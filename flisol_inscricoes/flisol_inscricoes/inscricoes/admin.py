from django.contrib import admin

from .models import Interesse, Participante


class InteresseAdmin(admin.ModelAdmin):
    pass


class ParticipanteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Interesse, InteresseAdmin)
admin.site.register(Participante, ParticipanteAdmin)
