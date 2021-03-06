# Generated by Django 2.2.9 on 2020-10-09 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swansoftapp', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, max_length=8)),
                ('cartitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swansoftapp.CartItem')),
            ],
        ),
    ]
