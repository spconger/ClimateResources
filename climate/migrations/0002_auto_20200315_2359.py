# Generated by Django 2.2.6 on 2020-03-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
