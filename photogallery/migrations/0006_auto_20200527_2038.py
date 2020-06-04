# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-27 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0005_auto_20200527_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=244)),
                ('country', models.CharField(max_length=244)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('description', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='photos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='image',
        ),
        migrations.RemoveField(
            model_name='album',
            name='tags',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=144),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='tags',
        ),
        migrations.AddField(
            model_name='photo',
            name='categories',
            field=models.ManyToManyField(to='photogallery.Category'),
        ),
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photogallery.Location'),
        ),
    ]
