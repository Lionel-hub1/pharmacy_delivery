# Generated by Django 5.0.1 on 2024-02-07 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_medicine_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='ratings',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]