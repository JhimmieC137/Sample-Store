# Generated by Django 4.0.7 on 2022-09-20 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='phone',
        ),
    ]