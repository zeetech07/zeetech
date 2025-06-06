# Generated by Django 5.1.1 on 2025-02-26 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0005_remove_footer_our_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('broucher_desc', models.TextField()),
                ('file', models.FileField(upload_to='brouchers/')),
                ('broucher_uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.course')),
            ],
        ),
    ]
