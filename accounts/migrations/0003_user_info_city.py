# Generated by Django 5.0.1 on 2024-01-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_info_agree'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]