# Generated by Django 5.0.1 on 2024-02-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_info_city'),
        ('products', '0002_alter_product_options_alter_product_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='product_favorites',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
