# Generated by Django 4.0.2 on 2022-11-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_tweets'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
