# Generated by Django 2.0.5 on 2018-08-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigBasket', '0003_checklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_items',
            field=models.IntegerField(default=1),
        ),
    ]