# Generated by Django 4.1.4 on 2022-12-07 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.CharField(default='No Image Available', max_length=255),
        ),
    ]
