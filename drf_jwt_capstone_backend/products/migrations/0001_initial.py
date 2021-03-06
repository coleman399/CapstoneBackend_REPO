# Generated by Django 3.2.8 on 2022-01-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('salesPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('manufacturingCost', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('aisleName', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
