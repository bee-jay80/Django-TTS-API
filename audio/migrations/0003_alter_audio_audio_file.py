# Generated by Django 5.1.2 on 2024-10-22 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0002_alter_audio_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(blank=True, upload_to='audio-file/'),
        ),
    ]
