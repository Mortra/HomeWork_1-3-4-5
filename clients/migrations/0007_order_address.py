# Generated by Django 4.1 on 2022-08-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_alter_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
