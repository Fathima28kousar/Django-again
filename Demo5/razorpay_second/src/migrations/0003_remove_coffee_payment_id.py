# Generated by Django 5.0.3 on 2024-03-20 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_coffee_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coffee',
            name='payment_id',
        ),
    ]
