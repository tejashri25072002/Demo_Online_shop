# Generated by Django 4.2.7 on 2023-12-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecartapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Mobiles'), (2, 'Shoes'), (3, 'Clothes')], verbose_name='category'),
        ),
    ]
