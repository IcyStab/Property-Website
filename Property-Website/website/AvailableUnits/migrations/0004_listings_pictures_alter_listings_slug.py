# Generated by Django 4.1.4 on 2023-02-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvailableUnits', '0003_alter_listings_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='pictures',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='slug',
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]