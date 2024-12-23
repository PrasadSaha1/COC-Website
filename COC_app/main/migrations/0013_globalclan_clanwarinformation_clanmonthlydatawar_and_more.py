# Generated by Django 5.1.3 on 2024-12-22 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_playermonthlydata_attack_wins_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalClan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clan_tag', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClanWarInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('war_info', models.JSONField(default=list)),
                ('clan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='war_information', to='main.globalclan')),
            ],
        ),
        migrations.CreateModel(
            name='ClanMonthlyDataWar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_wars', models.FloatField(default=0.0)),
                ('total_players', models.FloatField(default=0.0)),
                ('total_stars', models.FloatField(default=0.0)),
                ('total_destruction', models.FloatField(default=0.0)),
                ('clan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_data_war', to='main.globalclan')),
            ],
        ),
        migrations.CreateModel(
            name='ClanMonthlyDataGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_data_general', to='main.globalclan')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerMonthlyDataWar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_wars', models.IntegerField()),
                ('num_attacks', models.IntegerField()),
                ('num_missed_attacks', models.IntegerField()),
                ('total_stars', models.IntegerField()),
                ('total_destruction', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_data_war', to='main.globalplayer')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerWarInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateField()),
                ('clan_name', models.CharField(max_length=50)),
                ('clan_tag', models.CharField(max_length=20)),
                ('roster_number', models.IntegerField()),
                ('num_attacks', models.IntegerField()),
                ('attack_1_stars', models.IntegerField()),
                ('attack_1_percent', models.IntegerField()),
                ('attack_2_stars', models.IntegerField()),
                ('attack_2_percent', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='war_information', to='main.globalplayer')),
            ],
        ),
    ]
