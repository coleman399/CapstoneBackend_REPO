# Generated by Django 3.2.8 on 2021-12-17 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('Customer', 'Customer'), ('Administrator', 'Administrator')], max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='role_name',
            field=models.ManyToManyField(to='authentication.Role'),
        ),
    ]
