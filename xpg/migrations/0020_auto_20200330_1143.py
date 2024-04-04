# Generated by Django 3.0.4 on 2020-03-30 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0019_buyer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='address1',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='state',
        ),
    ]
