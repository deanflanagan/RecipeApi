# Generated by Django 3.1.7 on 2021-03-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210330_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ManyToManyField(to='api.Recipe'),
        ),
    ]