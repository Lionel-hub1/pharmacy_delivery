# Generated by Django 5.0.1 on 2024-02-07 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_medicine_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]