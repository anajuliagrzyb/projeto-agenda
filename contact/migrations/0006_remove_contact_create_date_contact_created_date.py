# Generated by Django 5.2.3 on 2025-06-30 14:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='create_date',
        ),
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
