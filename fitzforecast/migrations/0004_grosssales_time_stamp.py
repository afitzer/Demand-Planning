# Generated by Django 3.2.18 on 2023-04-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitzforecast', '0003_remove_product_gross_sales_remove_product_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grosssales',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default='2023-04-01'),
            preserve_default=False,
        ),
    ]
