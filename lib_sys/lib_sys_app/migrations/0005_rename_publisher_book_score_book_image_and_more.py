# Generated by Django 5.0.6 on 2024-06-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_sys_app', '0004_remove_book_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='score',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='book-image.jpg', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(max_length=200),
        ),
    ]