# Generated by Django 2.0.3 on 2019-05-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20190504_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.99', max_digits=6),
        ),
    ]
