# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-20 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('password', models.CharField(max_length=255, verbose_name='\u041a\u043e\u0434 \u0434\u043b\u044f \u0430\u043b\u044c\u0431\u043e\u043c\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u0430\u043b\u044c\u0431\u043e\u043c',
                'verbose_name_plural': '\u0413\u043b\u0430\u0432\u043d\u044b\u0435 \u0430\u043b\u044c\u0431\u043e\u043c\u044b',
            },
        ),
        migrations.CreateModel(
            name='FolderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('main_folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload_app.Folder', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0433\u043b\u0430\u0432\u044b\u0439 \u0430\u043b\u044c\u0431\u043e\u043c')),
            ],
            options={
                'verbose_name': '\u0410\u043b\u0431\u043e\u043c',
                'verbose_name_plural': '\u0410\u043b\u044c\u0431\u043e\u043c\u044b \u043f\u0430\u043f\u043e\u043a',
            },
        ),
        migrations.AddField(
            model_name='folderimage',
            name='subfolder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload_app.SubFolder', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u043b\u044c\u0431\u043e\u043c'),
        ),
    ]
