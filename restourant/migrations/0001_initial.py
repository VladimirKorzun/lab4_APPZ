# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 22:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=150)),
                ('date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=150)),
                ('image', models.ImageField(blank=True, help_text='150x150px', upload_to='static/images/', verbose_name='Ссылка картинки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restouran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=150)),
                ('image', models.ImageField(blank=True, help_text='150x150px', upload_to='static/images/', verbose_name='Ссылка картинки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restourant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='restourant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restourant.Restouran'),
        ),
        migrations.AddField(
            model_name='comment',
            name='restourant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restourant.Restouran'),
        ),
    ]
