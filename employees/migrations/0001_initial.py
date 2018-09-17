# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-09-17 06:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='email')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True, verbose_name='first name')),
                ('lastname', models.CharField(blank=True, max_length=50, null=True, verbose_name='last name')),
                ('headline', models.CharField(blank=True, max_length=70, null=True, verbose_name='headline')),
                ('website', models.URLField(blank=True, max_length=70, null=True, verbose_name='website')),
                ('linkedin', models.URLField(blank=True, max_length=70, null=True, verbose_name='linkedin')),
                ('github', models.URLField(blank=True, max_length=70, null=True, verbose_name='github')),
                ('twitter', models.URLField(blank=True, max_length=70, null=True, verbose_name='twitter')),
                ('angelist', models.URLField(blank=True, max_length=70, null=True, verbose_name='angelist')),
                ('blog', models.URLField(blank=True, max_length=70, null=True, verbose_name='blog')),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('skills', models.TextField(blank=True, null=True, verbose_name='skills')),
                ('achivements', models.TextField(blank=True, null=True, verbose_name='achivements')),
                ('company', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
    ]
