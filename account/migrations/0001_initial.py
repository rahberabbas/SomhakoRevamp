# Generated by Django 4.0.6 on 2022-07-11 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='employee', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=256, null=True)),
                ('last_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
            bases=('account.user',),
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='employer', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Employer',
                'verbose_name_plural': 'Employers',
            },
            bases=('account.user',),
        ),
    ]
