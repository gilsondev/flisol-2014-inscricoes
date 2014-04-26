from django.contrib import admin

from .models import Interesse, Oficina, Participante


class InteresseAdmin(admin.ModelAdmin):
    pass


class ParticipanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criacao'
    list_display = ('nome', 'email', 'telefone', 'campeonato_games', 'criacao',
                    'atualizacao')
    list_filter = ('campeonato_games', 'oficinas', 'interesses', 'atualizacao')
    search_fields = ('nome', 'representacao', 'email')


class OficinaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Interesse, InteresseAdmin)
admin.site.register(Oficina, OficinaAdmin)
admin.site.register(Participante, ParticipanteAdmin)
