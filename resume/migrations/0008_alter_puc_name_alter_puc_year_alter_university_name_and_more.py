# Generated by Django 4.2.2 on 2023-08-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_alter_account_facebook_alter_account_pinterest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puc',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='puc',
            name='year',
            field=models.CharField(blank=True, default=None, max_length=6),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='university',
            name='year',
            field=models.CharField(blank=True, default=None, max_length=6),
        ),
    ]