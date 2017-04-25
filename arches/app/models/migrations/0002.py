# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-24 13:08
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maplayer',
            name='centerx',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maplayer',
            name='centery',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maplayer',
            name='zoom',
            field=models.FloatField(blank=True, null=True),
        )
    ]

    migrations.RunSQL(
            """
            INSERT INTO widgets(widgetid, name, component, datatype, defaultconfig) VALUES ('10000000-0000-0000-0000-000000000020', 'csv-chart-widget', 'views/components/widgets/csv-chart', 'csv-chart-json', '{"acceptedFiles": "", "maxFilesize": "200"}');
            INSERT INTO d_data_types VALUES ('csv-chart-json', 'fa fa-line-chart', 'datatypes.py', 'CSVChartJsonDataType', null, null, null, FALSE, '10000000-0000-0000-0000-000000000020');
            UPDATE d_data_types SET (modulename) = ('datatypes.py') WHERE datatype in ('domain-value', 'domain-value-list');
            """
            ),
