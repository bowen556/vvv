# Generated by Django 2.2.9 on 2020-07-06 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20200705_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locations',
            old_name='STS_lautitude_position',
            new_name='STS_latitude',
        ),
        migrations.RenameField(
            model_name='locations',
            old_name='STS_longitude_position',
            new_name='STS_longitude',
        ),
    ]