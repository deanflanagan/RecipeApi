# Generated by Django 2.2.5 on 2021-04-03 23:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210331_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', to='api.Ingredient', validators=[django.core.validators.MinValueValidator(2)]),
        ),
    ]
