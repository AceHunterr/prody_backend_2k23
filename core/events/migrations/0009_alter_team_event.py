# Generated by Django 4.0.8 on 2023-09-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_team_team_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='events.event'),
        ),
    ]