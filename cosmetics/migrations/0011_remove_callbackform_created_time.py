# Generated by Django 4.1.3 on 2023-01-05 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetics', '0010_callbackform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callbackform',
            name='created_time',
        ),
    ]
