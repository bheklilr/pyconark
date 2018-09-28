# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-25 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavBarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(max_length=36)),
                ('slug', models.SlugField(blank=True)),
                ('destinationPath', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('LABEL', 'LABEL'), ('DROPDOWN', 'DROPDOWN'), ('HREF', 'HREF')], default='LABEL', max_length=255)),
                ('sortOrder', models.IntegerField(default=10)),
                ('isActive', models.BooleanField(default=False)),
                ('parentItem', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.NavBarItem')),
            ],
        ),
        migrations.AlterField(
            model_name='conferencelocation',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
