# Generated by Django 5.0.3 on 2024-04-15 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='futureevent',
            old_name='donation_center_id',
            new_name='donation_center',
        ),
    ]