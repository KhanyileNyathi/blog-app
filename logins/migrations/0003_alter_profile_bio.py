# Generated by Django 5.0 on 2024-01-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0002_profile_follows_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]