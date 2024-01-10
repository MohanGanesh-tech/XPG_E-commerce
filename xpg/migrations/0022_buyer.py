# Generated by Django 3.0.4 on 2020-03-30 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0021_delete_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('uid', models.IntegerField()),
                ('productname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postcode', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
