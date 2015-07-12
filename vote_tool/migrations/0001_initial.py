# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import vote_tool.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vote', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Votes',
            },
        ),
        migrations.CreateModel(
            name='VoteChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Approved?')),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Voting Choice',
                'verbose_name_plural': 'Voting Choices',
            },
        ),
        migrations.CreateModel(
            name='VotingTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('description', models.TextField(null=True, blank=True)),
                ('list_page_view', vote_tool.fields.MultiSelectField(default=[1, 2], max_length=250, blank=True, choices=[(1, 'Allow List View'), (2, 'Allow Card View')])),
                ('list_page_voting', models.BooleanField(default=False, verbose_name='Allow voting on the list page.')),
                ('anonymous_voting', models.BooleanField(default=False, verbose_name='Allow anonymous voting')),
                ('voting_enabled_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('require_approval', models.BooleanField(default=True, verbose_name='Vote Choice Submission Requires Approval')),
            ],
            options={
                'verbose_name': 'Voting Topic',
                'verbose_name_plural': 'Voting Topics',
            },
        ),
        migrations.AddField(
            model_name='votechoice',
            name='topic',
            field=models.ForeignKey(to='vote_tool.VotingTopic'),
        ),
        migrations.AddField(
            model_name='votechoice',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='choice',
            field=models.ForeignKey(to='vote_tool.VoteChoice'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
