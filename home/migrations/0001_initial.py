# Generated by Django 4.1.1 on 2022-09-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_name', models.CharField(max_length=125)),
                ('Department', models.CharField(max_length=125)),
                ('Active_employees', models.CharField(max_length=125)),
                ('Status', models.CharField(max_length=125)),
            ],
        ),
    ]
