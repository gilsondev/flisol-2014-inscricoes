from django import forms
from django.forms import CheckboxSelectMultiple
from django.db.models import Count

from models import Participante, Oficina

LIMITE_VAGAS_OFICINA = 8
LIMITE_VAGAS_GAMES = 24


class ParticipanteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ParticipanteForm, self).__init__(*args, **kwargs)
        oficinas_lotadas = Oficina.objects.annotate(
            count_participantes=Count('participante')
        ).values(
            'pk',
            'count_participantes'
        ).filter(
            count_participantes__gte=LIMITE_VAGAS_OFICINA
        )
        exclude_oficinas = [oficina.get('pk') for oficina in oficinas_lotadas]
        queryset = Oficina.objects.exclude(pk__in=exclude_oficinas)
        self.fields['oficinas'].queryset = queryset

        contagem = Participante.objects.filter(campeonato_games=True).count()
        if contagem >= LIMITE_VAGAS_GAMES:
            self.fields['campeonato_games'].widget = forms.HiddenInput()

    class Meta:
        model = Participante
        widgets = {
            'interesses': CheckboxSelectMultiple(),
            'oficinas': CheckboxSelectMultiple(),
        }
