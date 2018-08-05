# Generated by Django 2.0.5 on 2018-08-05 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BigBasket', '0013_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_cost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BigBasket.Product'),
        ),
    ]