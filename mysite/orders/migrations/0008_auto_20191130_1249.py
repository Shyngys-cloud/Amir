# Generated by Django 2.2.7 on 2019-11-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20191130_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.CharField(choices=[('GLOVO + 1000', 'GLOVO'), ('YANDEX + 900', 'YANDEX'), ('WOLT + 1100', 'WOLT')], default='GLOVO + 1000', max_length=10, verbose_name='Доставка'),
        ),
    ]