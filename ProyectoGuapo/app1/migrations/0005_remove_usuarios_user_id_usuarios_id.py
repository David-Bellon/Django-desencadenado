# Generated by Django 4.0.2 on 2022-03-22 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_usuarios_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='user_id',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
