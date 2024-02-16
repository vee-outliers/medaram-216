# Generated by Django 3.2.5 on 2024-02-15 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_user_is_first_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointdata',
            name='region',
        ),
        migrations.RemoveField(
            model_name='pointdata',
            name='zone',
        ),
        migrations.AddField(
            model_name='depot',
            name='depot_sno',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='depot',
            name='region',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='depot',
            name='zone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='AllotmentOfBuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_buses', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(blank=True, help_text='0=active;1=inactive;2=delete', null=True)),
                ('created_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allotment_buses_created_user', to='app.user')),
                ('operating_depot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allotment_buses_operating_depot', to='app.depot')),
                ('parent_depot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allotment_buses_parent_depot', to='app.depot')),
                ('updated_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allotment_buses_updated_user', to='app.user')),
            ],
        ),
    ]
