# Generated by Django 3.0.8 on 2020-08-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoptions',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
    ]
