# Generated by Django 4.0.2 on 2022-02-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
