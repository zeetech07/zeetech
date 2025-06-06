# Generated by Django 5.1.1 on 2025-03-06 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0010_userreg_placement_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(blank=True, limit_choices_to={'user__role': 'student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, limit_choices_to={'user__role': 'student'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.userreg'),
        ),
    ]
