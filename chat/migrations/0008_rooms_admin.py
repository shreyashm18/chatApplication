# Generated by Django 3.0.1 on 2020-10-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20201007_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='admin',
            field=models.CharField(default='Shreyash', max_length=255),
        ),
    ]
