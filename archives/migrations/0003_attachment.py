# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 17:49
from __future__ import unicode_literals

import archives.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archives', '0002_auto_20161004_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to=archives.models.generate_random_filename, verbose_name='文件')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='上传者')),
            ],
            options={
                'ordering': ['-created_time'],
                'verbose_name': '附件',
                'verbose_name_plural': '附件',
            },
        ),
    ]