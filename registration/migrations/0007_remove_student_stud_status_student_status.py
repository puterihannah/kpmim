# Generated by Django 5.1.3 on 2024-12-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_remove_student_status_student_stud_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stud_status',
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='MP', max_length=3),
        ),
    ]
