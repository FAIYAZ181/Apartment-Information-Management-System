# Generated by Django 3.1.7 on 2021-04-12 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OurProject', '0002_auto_20210412_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartments',
            name='user_id',
        ),
    ]
