# Generated by Django 3.0.4 on 2020-03-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0025_csmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecmodel',
            name='category',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eemodel',
            name='category',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='melmodel',
            name='category',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memodel',
            name='category',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='othermodel',
            name='category',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tcmodel',
            name='category',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xprojectmodel',
            name='category',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]