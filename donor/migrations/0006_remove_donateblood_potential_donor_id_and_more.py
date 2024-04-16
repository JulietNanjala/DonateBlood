# Generated by Django 5.0.3 on 2024-04-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0005_remove_donationhistory_potential_donor_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donateblood',
            name='potential_donor_id',
        ),
        migrations.AddField(
            model_name='donateblood',
            name='email_address',
            field=models.EmailField(default=None, help_text='Enter a valid email address', max_length=200, unique=True),
        ),
    ]
