# Generated by Django 4.2.2 on 2023-08-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_puc_institute_skill_lang_sslc_institute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
    ]
