# Generated by Django 3.1.7 on 2021-05-02 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OurProject', '0003_remove_apartments_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartments',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OurProject.user'),
        ),
    ]