# Generated by Django 2.2.12 on 2020-04-26 23:30

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to='games')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to='editions')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck_crafter.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), help_text='Use a comma to separate tags in the edit form field.', size=None)),
                ('text', models.TextField()),
                ('image', sorl.thumbnail.fields.ImageField(null=True, upload_to='cards')),
                ('artist', models.CharField(blank=True, max_length=256)),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck_crafter.Edition')),
            ],
        ),
    ]
