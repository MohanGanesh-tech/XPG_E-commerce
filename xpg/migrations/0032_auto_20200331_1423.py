# Generated by Django 3.0.4 on 2020-03-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0031_auto_20200331_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='star',
            field=models.TextField(),
        ),
    ]
