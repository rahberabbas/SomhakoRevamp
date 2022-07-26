# Generated by Django 4.0.6 on 2022-07-20 08:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_employee_mobile'),
        ('jobapp', '0027_alter_applicant_final_status_alter_applicant_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='jobapp.department'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(blank=True, choices=[('5', 'Completed'), ('3', 'In-Progress'), ('1', 'In-Review'), ('4', 'On-Hold'), ('6', 'Rejected'), ('2', 'Shortlist')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='second_status',
            field=models.CharField(blank=True, choices=[('2', 'Reject'), ('1', 'Passed'), ('3', 'On-Hold')], max_length=1),
        ),
        migrations.AlterField(
            model_name='interview',
            name='status',
            field=models.CharField(blank=True, choices=[('2', 'Reject'), ('1', 'Hire'), ('3', 'Hold')], max_length=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='experince',
            field=models.CharField(blank=True, choices=[('3', '5+ Yrs'), ('2', '2-4 Yrs'), ('1', '0-2 Yrs')], max_length=1),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=20)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('skill', models.CharField(blank=True, help_text='comma for new tags', max_length=2000, null=True)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dept', to='jobapp.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.employer')),
            ],
        ),
    ]
