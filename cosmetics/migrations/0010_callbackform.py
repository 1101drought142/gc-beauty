# Generated by Django 4.1.3 on 2023-01-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetics', '0009_alter_item_similar_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('phone', models.CharField(max_length=25)),
                ('created_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
