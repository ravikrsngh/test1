# Generated by Django 2.0.9 on 2020-06-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='lang',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
