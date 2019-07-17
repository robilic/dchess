# Generated by Django 2.1.10 on 2019-07-16 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20190316_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoveHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move', models.IntegerField()),
                ('black', models.CharField(max_length=6)),
                ('white', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='move',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movehistory',
            name='game',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='game', to='games.Game'),
        ),
    ]