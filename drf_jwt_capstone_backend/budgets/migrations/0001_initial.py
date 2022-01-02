# Generated by Django 3.2.8 on 2022-01-02 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_sales', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('total_expenses', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('total_profit', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
            ],
        ),
    ]
