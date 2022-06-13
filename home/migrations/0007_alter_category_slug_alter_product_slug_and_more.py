# Generated by Django 4.0.4 on 2022-06-09 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_slig_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.TextField(unique=True),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('slug', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(default=1)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
