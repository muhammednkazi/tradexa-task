# Generated by Django 3.0.6 on 2020-05-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200530_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
