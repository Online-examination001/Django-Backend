# Generated by Django 3.0.4 on 2020-04-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200408_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name=' username'),
        ),
    ]
