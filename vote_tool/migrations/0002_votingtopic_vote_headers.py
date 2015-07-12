# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vote_tool.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vote_tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingtopic',
            name='vote_headers',
            field=vote_tool.fields.VoteHeaderField(null=True, blank=True),
        ),
    ]
