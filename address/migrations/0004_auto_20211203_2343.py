# Generated by Django 3.2.9 on 2021-12-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_alter_address_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='line2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=5),
        ),
    ]
