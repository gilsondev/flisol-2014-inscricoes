from django import forms
from django.forms import CheckboxSelectMultiple

from models import Participante


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        widgets = {
            'interesses': CheckboxSelectMultiple(),
        }
