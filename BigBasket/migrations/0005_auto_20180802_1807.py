# Generated by Django 2.0.5 on 2018-08-02 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BigBasket', '0004_auto_20180802_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total_items',
            new_name='quantity',
        ),
    ]
