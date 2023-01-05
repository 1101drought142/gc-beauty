# Generated by Django 4.1.3 on 2022-12-18 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetics', '0003_alter_itemcategories_father_categorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='type',
            new_name='types',
        ),
        migrations.AlterField(
            model_name='item',
            name='Meta_description',
            field=models.CharField(max_length=120, verbose_name='meta description товара'),
        ),
        migrations.AlterField(
            model_name='item',
            name='Meta_keywords',
            field=models.CharField(max_length=60, verbose_name='meta keywords товара'),
        ),
        migrations.AlterField(
            model_name='item',
            name='Meta_title',
            field=models.CharField(max_length=30, verbose_name='meta title товара'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='Meta_description',
            field=models.CharField(max_length=120, verbose_name='meta description категории'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='Meta_keywords',
            field=models.CharField(max_length=60, verbose_name='meta keywords категории'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='Meta_title',
            field=models.CharField(max_length=30, verbose_name='meta title категории'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='father_categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cosmetics.itemcategories', verbose_name='Родительская категория'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='picture',
            field=models.FileField(upload_to='uploads/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='slug',
            field=models.CharField(max_length=30, verbose_name='Сокращение для ссылки'),
        ),
        migrations.AlterField(
            model_name='itemcategories',
            name='sort',
            field=models.IntegerField(verbose_name='Индекс сортировки'),
        ),
    ]