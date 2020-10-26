# -*- coding: utf-8 -*-
from django.db import models


class Produto(models.Model):

    nome = models.CharField('Nome', max_length=100)
    cor = models.CharField('Cor', max_length=100)
    codigo_gtin = models.CharField('Código', max_length=100)
    tipo = models.CharField('Tipo', max_length=100)
    processado = models.BooleanField(verbose_name='Processado',
                                    default=False)

    class Meta():
        app_label = 'base'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        super(Produto, self).save()

    def __str__(self):
        return u'%s ' % (self.nome)
