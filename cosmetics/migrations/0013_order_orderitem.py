# Generated by Django 4.1.3 on 2023-01-06 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetics', '0012_callbackform_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('mail', models.CharField(max_length=60, verbose_name='Email')),
                ('phone', models.CharField(max_length=60, verbose_name='Телефон')),
                ('city', models.CharField(max_length=60, verbose_name='Город')),
                ('street', models.CharField(max_length=60, verbose_name='Улица')),
                ('index', models.IntegerField(verbose_name='Индекс')),
                ('house', models.IntegerField(verbose_name='Номер дома')),
                ('flat', models.IntegerField(verbose_name='Номер квартиры')),
                ('payment_type', models.CharField(max_length=60, verbose_name='Способ оплаты')),
                ('created_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cosmetics.item', verbose_name='Товар')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cosmetics.order')),
            ],
        ),
    ]
