# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, unicode_literals

from django.db import models


class Interesse(models.Model):
    label = models.CharField('Interesse', max_length=80)

    def __unicode__(self):
        return self.label

    class Meta:
        verbose_name = 'Interesse'
        verbose_name_plural = 'Interesses'
        ordering = ['label']


class Oficina(models.Model):
    titulo = models.CharField('Título', max_length=80)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'


class Participante(models.Model):
    nome = models.CharField('Nome', max_length=140)
    representacao = models.CharField('Instituição / Empresa / Comunidade',
                                     max_length=80, blank=True)
    email = models.EmailField('E-mail', max_length=140, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=80, blank=True)
    interesses = models.ManyToManyField('inscricoes.Interesse',
                                        verbose_name='Interesses')
    outros_interesses = models.CharField('Outros interesses', max_length=140,
                                         blank=True)
    oficinas = models.ManyToManyField(
        'inscricoes.Oficina',
        verbose_name='Oficinas',
        blank=True,
        null=True,
        help_text='(Vagas Limitadas) Marque somente se quiser participar.'
    )
    campeonato_games = models.BooleanField(
        'Vai participar do campeonato de games?',
        blank=True,
        default=False,
        help_text='(Vagas Limitadas) Marque somente se quiser participar.'
    )

    criacao = models.DateTimeField('Data de cadastro', auto_now_add=True)
    atualizacao = models.DateTimeField('Data de atualização', auto_now=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ['criacao']
