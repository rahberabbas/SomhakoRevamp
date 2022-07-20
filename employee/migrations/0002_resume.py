# Generated by Django 4.0.6 on 2022-07-20 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_employee_mobile'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='company/logo/name/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.employer')),
            ],
        ),
    ]
