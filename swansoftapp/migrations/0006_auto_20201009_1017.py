# Generated by Django 2.2.9 on 2020-10-09 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swansoftapp', '0005_auto_20201009_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('accecpt', 'Accept'), ('reject', 'Reject')], default='pending', max_length=10),
        ),
    ]
