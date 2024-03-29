# Generated by Django 3.0.4 on 2020-03-28 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0004_eemodel_melmodel_memodel_tcmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='othermodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='xprojectmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
