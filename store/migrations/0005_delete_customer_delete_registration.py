# Generated by Django 4.0.7 on 2022-09-22 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_order_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
