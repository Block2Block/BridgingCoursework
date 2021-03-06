# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-22 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='full_body',
        ),
        migrations.AddField(
            model_name='post',
            name='short_body',
            field=models.CharField(default='Temp Short Body', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
