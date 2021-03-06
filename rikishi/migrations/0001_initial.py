# Generated by Django 3.1.2 on 2020-11-06 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rikishi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shikona_first', models.CharField(max_length=50)),
                ('shikona_last', models.CharField(max_length=50)),
                ('highest_rank', models.CharField(choices=[('Y', 'Yokozuna'), ('O', 'Ōzeki'), ('S', 'Sekiwake'), ('K', 'Komusubi'), ('M1', 'Maegashira 1'), ('M2', 'Maegashira 2'), ('M3', 'Maegashira 3'), ('M4', 'Maegashira 4'), ('M5', 'Maegashira 5'), ('M6', 'Maegashira 6'), ('M7', 'Maegashira 7'), ('M8', 'Maegashira 8'), ('M9', 'Maegashira 9'), ('M10', 'Maegashira 10'), ('M11', 'Maegashira 11'), ('M12', 'Maegashira 12'), ('M13', 'Maegashira 13'), ('M14', 'Maegashira 14'), ('M15', 'Maegashira 15'), ('M16', 'Maegashira 16'), ('M17', 'Maegashira 17'), ('M18', 'Maegashira 18')], default='Y', max_length=3)),
                ('total_wins', models.PositiveIntegerField()),
                ('total_losses', models.PositiveIntegerField()),
                ('total_absent', models.PositiveIntegerField()),
                ('real_name_first', models.CharField(max_length=50)),
                ('real_name_last', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('height', models.IntegerField(validators=[django.core.validators.MinValueValidator(150), django.core.validators.MaxValueValidator(250)])),
                ('weight', models.DecimalField(decimal_places=1, max_digits=4)),
                ('origin', models.CharField(max_length=100)),
            ],
        ),
    ]
