# Generated by Django 5.1 on 2024-10-08 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_laptop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='product_id',
            new_name='laptop_id',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='product_image',
            new_name='laptop_image',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='product_name',
            new_name='laptop_name',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='product_price',
            new_name='laptop_price',
        ),
    ]
