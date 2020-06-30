# Generated by Django 2.2.9 on 2020-06-29 18:13

import accounts.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200629_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Oil_Spill_Responders', models.CharField(blank=True, max_length=1000, null=True)),
                ('Local_Emergency_Medical_Assistance', models.CharField(blank=True, max_length=1000, null=True)),
                ('Police', models.CharField(blank=True, max_length=1000, null=True)),
                ('Coast_Guard', models.CharField(blank=True, max_length=1000, null=True)),
                ('Fire_fighting', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locations', djongo.models.fields.EmbeddedModelField(model_container=accounts.models.Locations, model_form_class=accounts.models.LocationsForm, null=True)),
                ('emergencycontacts', djongo.models.fields.EmbeddedModelField(model_container=accounts.models.EmergencyContacts, model_form_class=accounts.models.EmergencyContactsForm, null=True)),
                ('headline', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Emergency',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='Fendering_position',
        ),
        migrations.AddField(
            model_name='locations',
            name='Approval_needed_prior_to_each_STS_operation',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='Approval_to_conduct_STS_issued_by',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='Are_tugs_required',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='Cargos_permitted',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='Depth_of_water',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='Is_local_piloting_assistance_required',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='Night_time_berthing_permitted',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='Type_of_operation',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='Vessel_sizes_permitted',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]