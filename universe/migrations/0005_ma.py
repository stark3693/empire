# Generated by Django 4.0.5 on 2022-08-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0004_remove_galaxy_image_remove_galaxy_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='gal/images')),
            ],
        ),
    ]
