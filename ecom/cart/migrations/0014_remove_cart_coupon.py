# Generated by Django 4.1 on 2023-09-16 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_alter_cartitem_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='coupon',
        ),
    ]
