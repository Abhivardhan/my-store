# Generated by Django 2.0.5 on 2018-08-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigBasket', '0007_auto_20180802_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]