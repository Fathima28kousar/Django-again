# Generated by Django 5.0.3 on 2024-03-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]