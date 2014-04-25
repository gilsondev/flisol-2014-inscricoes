# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Oficina'
        db.create_table(u'inscricoes_oficina', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'inscricoes', ['Oficina'])

        # Adding field 'Participante.campeonato_games'
        db.add_column(u'inscricoes_participante', 'campeonato_games',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding M2M table for field oficinas on 'Participante'
        m2m_table_name = db.shorten_name(u'inscricoes_participante_oficinas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participante', models.ForeignKey(orm[u'inscricoes.participante'], null=False)),
            ('oficina', models.ForeignKey(orm[u'inscricoes.oficina'], null=False))
        ))
        db.create_unique(m2m_table_name, ['participante_id', 'oficina_id'])


    def backwards(self, orm):
        # Deleting model 'Oficina'
        db.delete_table(u'inscricoes_oficina')

        # Deleting field 'Participante.campeonato_games'
        db.delete_column(u'inscricoes_participante', 'campeonato_games')

        # Removing M2M table for field oficinas on 'Participante'
        db.delete_table(db.shorten_name(u'inscricoes_participante_oficinas'))


    models = {
        u'inscricoes.interesse': {
            'Meta': {'ordering': "[u'label']", 'object_name': 'Interesse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'inscricoes.oficina': {
            'Meta': {'object_name': 'Oficina'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'inscricoes.participante': {
            'Meta': {'ordering': "[u'criacao']", 'object_name': 'Participante'},
            'atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'campeonato_games': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interesses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inscricoes.Interesse']", 'symmetrical': 'False'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'oficinas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inscricoes.Oficina']", 'null': 'True', 'blank': 'True'}),
            'outros_interesses': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'representacao': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        }
    }

    complete_apps = ['inscricoes']