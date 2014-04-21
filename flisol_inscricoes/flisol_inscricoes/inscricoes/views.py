# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, unicode_literals

from django.contrib import messages
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from braces.views import SuccessURLRedirectListMixin

from .models import Participante
from .forms import ParticipanteForm


class CadastrarParticipante(SuccessURLRedirectListMixin, generic.CreateView):
    template_name = 'inscricoes/cadastrar-participante.html'
    model = Participante
    form_class = ParticipanteForm

    def get_success_url(self):
        messages.success(self.request, "Obrigado, agora você está cadastrado!")
        return reverse_lazy('inscricoes-cadastrar-participante')
