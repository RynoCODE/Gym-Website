# Generated by Django 5.0 on 2023-12-25 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_subscriber_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
