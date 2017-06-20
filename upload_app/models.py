# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import smart_unicode


class Folder(models.Model):
    class Meta:
        verbose_name_plural = 'Главные альбомы'
        verbose_name = 'Главный альбом'

    name = models.CharField(max_length=255, verbose_name='Наименование')
    password = models.CharField(max_length=255, verbose_name='Код для альбома')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class SubFolder(models.Model):
    class Meta:
        verbose_name_plural = 'Альбомы папок'
        verbose_name = 'Албом'

    name = models.CharField(max_length=255, verbose_name='Наименование')

    main_folder = models.ForeignKey(Folder, verbose_name='Выберите главый альбом')

    def __unicode__(self):
        return smart_unicode(self.name)


class FolderImage(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    subfolder = models.ForeignKey(SubFolder, verbose_name='Выберите альбом')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode('%s %s' % (self.subfolder.name, self.id))
