# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import vote_tool.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoteChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VotingTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
                ('list_page_view', vote_tool.models.MultiSelectField(default=[1, 2], max_length=250, blank=True, choices=[(1, b'Allow List View'), (2, b'Allow Card View')])),
                ('list_page_voting', models.BooleanField(default=False, verbose_name=b'Allow voting on the list page.')),
                ('voting_enabled_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='votechoice',
            name='topic',
            field=models.ForeignKey(to='vote_tool.VotingTopic'),
        ),
    ]
