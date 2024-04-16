# Generated by Django 5.0.3 on 2024-04-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0004_remove_donation_user_donation_potential_donor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationhistory',
            name='potential_donor_id',
        ),
        migrations.AddField(
            model_name='donationhistory',
            name='email_address',
            field=models.EmailField(default=None, help_text='Enter a valid email address', max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
