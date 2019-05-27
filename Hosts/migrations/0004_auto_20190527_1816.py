# Generated by Django 2.1.7 on 2019-05-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hosts', '0003_auto_20190422_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosts',
            name='descricao',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='porta',
            field=models.PositiveIntegerField(default=0),
        ),
    ]