# Generated by Django 3.0.4 on 2020-03-28 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0005_othermodel_xprojectmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='developermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]