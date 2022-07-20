# Generated by Django 4.0.6 on 2022-07-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0015_alter_applicant_final_status_alter_applicant_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='final_status',
            field=models.CharField(blank=True, choices=[('1', 'Hire'), ('2', 'Reject')], max_length=1),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'In-Review'), ('6', 'Rejected'), ('4', 'On-Hold'), ('3', 'In-Progress'), ('2', 'Shortlist'), ('5', 'Completed')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='second_status',
            field=models.CharField(blank=True, choices=[('1', 'Passed'), ('2', 'Failed')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.CharField(blank=True, choices=[('3', 'Hold'), ('1', 'Hire'), ('2', 'Reject')], max_length=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='experince',
            field=models.CharField(blank=True, choices=[('2', '2-4 Yrs'), ('3', '5+ Yrs'), ('1', '0-2 Yrs')], max_length=1),
        ),
    ]
