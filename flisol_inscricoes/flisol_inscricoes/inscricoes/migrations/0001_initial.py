# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Interesse'
        db.create_table(u'inscricoes_interesse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'inscricoes', ['Interesse'])

        # Adding model 'Participante'
        db.create_table(u'inscricoes_participante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('representacao', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=140, null=True, blank=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('outros_interesses', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'inscricoes', ['Participante'])

        # Adding M2M table for field interesses on 'Participante'
        m2m_table_name = db.shorten_name(u'inscricoes_participante_interesses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participante', models.ForeignKey(orm[u'inscricoes.participante'], null=False)),
            ('interesse', models.ForeignKey(orm[u'inscricoes.interesse'], null=False))
        ))
        db.create_unique(m2m_table_name, ['participante_id', 'interesse_id'])


    def backwards(self, orm):
        # Deleting model 'Interesse'
        db.delete_table(u'inscricoes_interesse')

        # Deleting model 'Participante'
        db.delete_table(u'inscricoes_participante')

        # Removing M2M table for field interesses on 'Participante'
        db.delete_table(db.shorten_name(u'inscricoes_participante_interesses'))


    models = {
        u'inscricoes.interesse': {
            'Meta': {'ordering': "[u'label']", 'object_name': 'Interesse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'inscricoes.participante': {
            'Meta': {'ordering': "[u'criacao']", 'object_name': 'Participante'},
            'atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interesses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inscricoes.Interesse']", 'symmetrical': 'False'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'outros_interesses': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'representacao': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        }
    }

    complete_apps = ['inscricoes']