# Generated by Django 2.1.7 on 2019-03-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_turn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='turn',
            field=models.IntegerField(default=1),
        ),
    ]