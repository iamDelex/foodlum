# Generated by Django 4.0.2 on 2022-03-07 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0008_alter_profile_cart_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
