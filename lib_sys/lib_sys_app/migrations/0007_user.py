# Generated by Django 5.0.6 on 2024-06-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_sys_app', '0006_auto_20240601_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('userpassword', models.CharField(max_length=16)),
            ],
        ),
    ]