# Generated by Django 4.0.6 on 2022-07-18 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_employee_mobile'),
        ('jobapp', '0019_alter_applicant_status_alter_interview_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'In-Review'), ('5', 'Completed'), ('6', 'Rejected'), ('2', 'Shortlist'), ('4', 'On-Hold'), ('3', 'In-Progress')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='second_status',
            field=models.CharField(blank=True, choices=[('1', 'Passed'), ('2', 'Failed')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.CharField(blank=True, choices=[('2', 'Reject'), ('3', 'Hold'), ('1', 'Hire')], max_length=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='experince',
            field=models.CharField(blank=True, choices=[('1', '0-2 Yrs'), ('3', '5+ Yrs'), ('2', '2-4 Yrs')], max_length=1),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.employer')),
            ],
        ),
    ]