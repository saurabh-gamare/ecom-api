# Generated by Django 4.1 on 2023-09-16 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_alter_cartitem_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
    ]
