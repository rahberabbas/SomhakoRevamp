# Generated by Django 4.0.6 on 2022-07-19 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0008_employerprofile_industry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employer.industry'),
        ),
    ]
