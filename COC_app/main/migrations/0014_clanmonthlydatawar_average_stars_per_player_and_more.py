# Generated by Django 5.1.3 on 2024-12-22 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_globalclan_clanwarinformation_clanmonthlydatawar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clanmonthlydatawar',
            name='average_stars_per_player',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='clanmonthlydatawar',
            name='average_total_destruction',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='clanmonthlydatawar',
            name='average_total_stars',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='clanmonthlydatawar',
            name='average_war_size',
            field=models.FloatField(default=0.0),
        ),
    ]