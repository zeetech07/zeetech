# Generated by Django 5.1.4 on 2025-02-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='social_media_link',
        ),
        migrations.AddField(
            model_name='footer',
            name='facebook',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='instagram',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='whatsapp',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
