# Generated by Django 5.0.3 on 2024-03-25 18:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_saleitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
