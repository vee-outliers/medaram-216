# Generated by Django 3.2.5 on 2024-02-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_depot_id_vehicledetails_depot'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_owner',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='vehicledetails',
            name='vehicle_owner',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
