# Generated by Django 3.2.9 on 2021-12-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20211204_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amazing', models.BooleanField(default=False)),
                ('meh', models.BooleanField(default=False)),
                ('terrible', models.BooleanField(default=False)),
            ],
        ),
    ]
