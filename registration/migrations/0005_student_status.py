# Generated by Django 5.1.3 on 2024-12-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='MP', max_length=3),
        ),
    ]
