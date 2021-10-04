# Generated by Django 3.2.7 on 2021-10-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podomarket', '0005_auto_20211004_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_condition',
            field=models.CharField(choices=[('새제품', '새제품'), ('최상', '최상'), ('상', '상'), ('중', '중'), ('하', '하')], default=None, max_length=10),
        ),
    ]
