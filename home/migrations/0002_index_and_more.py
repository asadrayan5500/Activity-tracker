# Generated by Django 4.0.5 on 2022-10-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(max_length=122)),
                ('Employee_id', models.CharField(max_length=122)),
                ('transaction_id', models.CharField(max_length=122)),
                ('status', models.CharField(max_length=122)),
            ],
        ),
        migrations.RenameField(
            model_name='activity_list',
            old_name='Active_employees',
            new_name='Activity_Id',
        ),
        migrations.RenameField(
            model_name='activity_list',
            old_name='Department',
            new_name='Create_date',
        ),
        migrations.RenameField(
            model_name='activity_list',
            old_name='Status',
            new_name='status',
        ),
    ]
