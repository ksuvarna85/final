# Generated by Django 3.0.7 on 2020-09-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO_App', '0004_reciept'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoprofile',
            name='description',
            field=models.CharField(default='-', max_length=600),
        ),
        migrations.AddField(
            model_name='ngoprofile',
            name='image',
            field=models.ImageField(default=1, upload_to='ngo_images'),
            preserve_default=False,
        ),
    ]