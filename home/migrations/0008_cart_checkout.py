# Generated by Django 4.0.4 on 2022-06-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_category_slug_alter_product_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
    ]
