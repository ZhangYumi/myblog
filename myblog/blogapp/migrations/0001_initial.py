# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=100)),
                ('art_datetime', models.DateTimeField(auto_now_add=True)),
                ('art_category', models.CharField(blank=True, max_length=50)),
                ('art_clicknum', models.IntegerField(null=True)),
                ('art_commentnum', models.IntegerField(null=True)),
                ('art_enjoylevel', models.CharField(max_length=1, null=True)),
                ('art_type', models.CharField(max_length=10, null=True)),
                ('art_imgurl', models.CharField(max_length=255, null=True)),
                ('art_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nickname', models.CharField(max_length=20)),
                ('user_job', models.CharField(max_length=50)),
                ('user_company', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=20)),
            ],
        ),
    ]
