# Generated by Django 2.0.13 on 2019-03-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0012_auto_20190306_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coachscout',
            name='match',
        ),
        migrations.RemoveField(
            model_name='matchscout',
            name='end_game',
        ),
        migrations.AddField(
            model_name='coachscout',
            name='match_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='hab_level',
            field=models.CharField(choices=[('0', 'None'), ('1', 'Hab Level 1'), ('2', 'Hab Level 2'), ('3', 'Hab Level 3')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='recommend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='strategy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='team_work',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='EndGame',
        ),
    ]
