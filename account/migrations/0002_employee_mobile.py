# Generated by Django 4.0.6 on 2022-07-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='mobile',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
