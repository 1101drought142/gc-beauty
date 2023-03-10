# Generated by Django 4.1.3 on 2022-12-18 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetics', '0004_rename_type_item_types_alter_item_meta_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='main_picture',
            field=models.FileField(default='/', upload_to='uploads/', verbose_name='Основаня фотография'),
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='uploads/', verbose_name='Фотография')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cosmetics.item')),
            ],
        ),
    ]
