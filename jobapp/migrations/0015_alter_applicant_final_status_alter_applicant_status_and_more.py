# Generated by Django 4.0.6 on 2022-07-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0014_remove_job_qualification_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='final_status',
            field=models.CharField(blank=True, choices=[('2', 'Reject'), ('1', 'Hire')], max_length=1),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(blank=True, choices=[('4', 'On-Hold'), ('5', 'Completed'), ('3', 'In-Progress'), ('6', 'Rejected'), ('1', 'In-Review'), ('2', 'Shortlist')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.CharField(blank=True, choices=[('2', 'Reject'), ('1', 'Hire'), ('3', 'Hold')], max_length=1),
        ),
    ]
