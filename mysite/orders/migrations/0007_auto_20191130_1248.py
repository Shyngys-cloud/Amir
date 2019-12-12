# Generated by Django 2.2.7 on 2019-11-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191130_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.CharField(choices=[('GLOVO', 'GLOVO'), ('YANDEX', 'YANDEX'), ('WOLT', 'WOLT')], default='GLOVO', max_length=10, verbose_name='Доставка'),
        ),
    ]
