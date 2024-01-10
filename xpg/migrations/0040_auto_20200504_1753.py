# Generated by Django 3.0.4 on 2020-05-04 12:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0039_delete_profiles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='othermodel',
            old_name='img',
            new_name='img1',
        ),
        migrations.AddField(
            model_name='othermodel',
            name='img2',
            field=models.ImageField(default=True, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='othermodel',
            name='img3',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='othermodel',
            name='img4',
            field=models.ImageField(default=True, upload_to='pics'),
            preserve_default=False,
        ),
    ]