# Generated by Django 3.2.8 on 2022-01-02 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userPassword',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
