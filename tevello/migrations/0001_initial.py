# Generated by Django 2.2.4 on 2019-08-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
