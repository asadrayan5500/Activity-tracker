# Generated by Django 4.0.5 on 2022-10-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_activitylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='logins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=22)),
                ('password', models.CharField(max_length=22)),
            ],
        ),
    ]
