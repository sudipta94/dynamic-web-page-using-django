# Generated by Django 2.2.4 on 2019-08-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tevello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
