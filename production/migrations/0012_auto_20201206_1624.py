# Generated by Django 3.1.2 on 2020-12-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0011_auto_20201110_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='production',
            name='climate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='ph_value',
            field=models.FloatField(null=True),
        ),
    ]
