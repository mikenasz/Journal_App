# Generated by Django 3.2.9 on 2021-12-06 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0003_mood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mood',
            name='amazing',
        ),
        migrations.RemoveField(
            model_name='mood',
            name='meh',
        ),
        migrations.RemoveField(
            model_name='mood',
            name='terrible',
        ),
        migrations.AddField(
            model_name='mood',
            name='mood',
            field=models.CharField(blank=True, choices=[('Amazing', 'Amazing'), ('Meh', 'Meh'), ('Terrible', 'Terrible')], max_length=20),
        ),
        migrations.AddField(
            model_name='mood',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
