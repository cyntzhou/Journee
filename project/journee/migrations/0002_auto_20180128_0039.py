# Generated by Django 2.0.1 on 2018-01-28 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traveler',
            old_name='facebook_username',
            new_name='email',
        ),
    ]
