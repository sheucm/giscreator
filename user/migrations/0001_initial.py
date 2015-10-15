# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gis',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('lat', models.CharField(max_length=12)),
                ('lon', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
