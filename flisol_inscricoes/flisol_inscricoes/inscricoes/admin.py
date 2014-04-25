from django.contrib import admin

from .models import Interesse, Oficina, Participante


class InteresseAdmin(admin.ModelAdmin):
    pass


class ParticipanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criacao'
    list_display = ('nome', 'representacao', 'email', 'telefone',
                    'campeonato_games', 'criacao', 'atualizacao')
    list_filter = ('nome', 'representacao', 'outros_interesses',
                   'campeonato_games', 'criacao', 'atualizacao')
    search_fields = ('nome', 'representacao', 'email')


class OficinaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Interesse, InteresseAdmin)
admin.site.register(Oficina, OficinaAdmin)
admin.site.register(Participante, ParticipanteAdmin)
