# Generated by Django 2.0.13 on 2019-03-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0013_auto_20190306_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingame',
            name='match',
        ),
        migrations.AlterModelOptions(
            name='robot',
            options={'ordering': ['robot_number']},
        ),
        migrations.AddField(
            model_name='matchscout',
            name='cargo_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='hatch_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchscout',
            name='in_match_actions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='InGame',
        ),
    ]
