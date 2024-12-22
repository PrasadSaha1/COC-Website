# Generated by Django 5.1.3 on 2024-12-21 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_playermonthlydata_year_alter_playermonthlydata_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playermonthlydata',
            name='total_levels',
        ),
        migrations.AddField(
            model_name='playermonthlydata',
            name='XP_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playermonthlydata',
            name='spell_data',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='playermonthlydata',
            name='troop_data',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='playermonthlydata',
            name='trophies',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playermonthlydata',
            name='war_stars',
            field=models.IntegerField(default=0),
        ),
    ]