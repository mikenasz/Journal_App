# Generated by Django 3.2.9 on 2021-12-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_auto_20211206_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='mood',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
