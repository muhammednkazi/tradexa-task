# Generated by Django 3.0.6 on 2020-05-30 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200531_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='users.user'),
        ),
    ]