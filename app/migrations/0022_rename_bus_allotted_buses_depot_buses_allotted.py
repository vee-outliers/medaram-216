# Generated by Django 3.2.5 on 2024-02-04 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_depot_bus_allotted_buses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='depot',
            old_name='bus_allotted_buses',
            new_name='buses_allotted',
        ),
    ]