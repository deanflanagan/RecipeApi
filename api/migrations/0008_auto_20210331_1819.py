# Generated by Django 3.1.7 on 2021-03-31 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_ingredient_meat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient',
            new_name='name',
        ),
    ]
