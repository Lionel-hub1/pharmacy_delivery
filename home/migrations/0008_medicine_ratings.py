# Generated by Django 5.0.1 on 2024-02-06 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_medicine_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='ratings',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
