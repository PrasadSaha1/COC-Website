# Generated by Django 5.1.3 on 2024-12-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_clanmonthlydatawar_percent_attacks_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clanmonthlydatawar',
            name='current_time',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
