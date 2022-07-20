# Generated by Django 4.0.6 on 2022-07-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_alter_applicant_status_alter_interview_status_and_more'),
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
            field=models.CharField(blank=True, choices=[('6', 'Rejected'), ('3', 'In-Progress'), ('5', 'Completed'), ('4', 'On-Hold'), ('2', 'Shortlist'), ('1', 'In-Review')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='second_status',
            field=models.CharField(blank=True, choices=[('2', 'Failed'), ('1', 'Passed')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.CharField(blank=True, choices=[('2', 'Reject'), ('1', 'Hire'), ('3', 'Hold')], max_length=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='experince',
            field=models.CharField(blank=True, choices=[('1', '0-2 Yrs'), ('3', '5+ Yrs'), ('2', '2-4 Yrs')], max_length=1),
        ),
    ]
