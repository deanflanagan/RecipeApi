# Generated by Django 2.2.5 on 2021-04-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210404_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='https://d3mvlb3hz2g78.cloudfront.net/wp-content/uploads/2013/04/thumb_720_450_920.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]