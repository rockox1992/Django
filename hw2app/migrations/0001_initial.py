# Generated by Django 4.2.5 on 2023-09-30 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('client_address', models.CharField(max_length=200)),
                ('registration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_goods', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('date_added', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ordergds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_added', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw2app.client')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw2app.goods')),
            ],
        ),
    ]
