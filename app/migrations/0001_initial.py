# Generated by Django 5.0.1 on 2024-01-16 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('year', models.IntegerField(default=0)),
                ('cover_url', models.URLField(default='')),
                ('available_in_pdf', models.BooleanField(default=False)),
                ('pdf_url', models.URLField(blank=True, default='', null=True)),
                ('available_in_epub', models.BooleanField(default=False)),
                ('epub_url', models.URLField(blank=True, default='', null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
            ],
        ),
    ]
