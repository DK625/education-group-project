# Generated by Django 5.0.7 on 2024-09-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question_images/'),
        ),
    ]
