# Generated by Django 3.0.4 on 2020-03-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]