# Generated by Django 4.0.6 on 2022-07-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0004_alter_applicant_final_status_alter_applicant_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(blank=True, choices=[('2', 'Shortlist'), ('1', 'In-Review'), ('5', 'Completed'), ('3', 'In-Progress'), ('4', 'On-Hold'), ('6', 'Rejected')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.CharField(blank=True, choices=[('2', 'Reject'), ('1', 'Hire'), ('3', 'Hold')], max_length=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='experince',
            field=models.CharField(blank=True, choices=[('2', '2-4 Yrs'), ('3', '5+ Yrs'), ('1', '0-2 Yrs')], max_length=1),
        ),
    ]
