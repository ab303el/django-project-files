# Generated by Django 5.1.2 on 2024-12-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0005_jobposting_jobcategories'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcategories',
            name='images',
            field=models.ImageField(default='empty', upload_to='images/'),
        ),
    ]
