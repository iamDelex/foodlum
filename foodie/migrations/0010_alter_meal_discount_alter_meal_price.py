# Generated by Django 4.0.2 on 2022-03-07 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0009_alter_meal_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='discount',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.CharField(default=0, max_length=50),
        ),
    ]