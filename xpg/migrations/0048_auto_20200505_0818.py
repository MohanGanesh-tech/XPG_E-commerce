# Generated by Django 3.0.4 on 2020-05-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpg', '0047_auto_20200505_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='othermodel',
            old_name='img1',
            new_name='img',
        ),
        migrations.AddField(
            model_name='csmodel',
            name='img2',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='csmodel',
            name='img3',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='csmodel',
            name='img4',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='csmodel',
            name='img5',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='ecmodel',
            name='img2',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='ecmodel',
            name='img3',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='ecmodel',
            name='img4',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='ecmodel',
            name='img5',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='eemodel',
            name='img2',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='eemodel',
            name='img3',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='eemodel',
            name='img4',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='eemodel',
            name='img5',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='melmodel',
            name='img2',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='melmodel',
            name='img3',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='melmodel',
            name='img4',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='melmodel',
            name='img5',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='memodel',
            name='img2',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='memodel',
            name='img3',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='memodel',
            name='img4',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='memodel',
            name='img5',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='tcmodel',
            name='img2',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='tcmodel',
            name='img3',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='tcmodel',
            name='img4',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='tcmodel',
            name='img5',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='xprojectmodel',
            name='img2',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='xprojectmodel',
            name='img3',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='xprojectmodel',
            name='img4',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='xprojectmodel',
            name='img5',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='othermodel',
            name='img2',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='othermodel',
            name='img3',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='othermodel',
            name='img4',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='othermodel',
            name='img5',
            field=models.ImageField(blank=True, default='False', upload_to='pics'),
        ),
    ]