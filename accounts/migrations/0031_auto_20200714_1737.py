# Generated by Django 2.2.9 on 2020-07-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_blacklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='STS_latitude',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='STS_longitude',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='STS_position',
        ),
        migrations.AddField(
            model_name='entry',
            name='STS_Latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='STS_Longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='degrees_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='degrees_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='minutes_latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='minutes_longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='seconds_latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='seconds_longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
