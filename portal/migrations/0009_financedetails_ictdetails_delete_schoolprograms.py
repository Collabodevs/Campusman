# Generated by Django 4.0 on 2022-10-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_studentdetails_faculty_alter_studentdetails_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Finance Officers',
            },
        ),
        migrations.CreateModel(
            name='ICTDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'ICT Personnels',
            },
        ),
        migrations.DeleteModel(
            name='SchoolPrograms',
        ),
    ]
