# Generated by Django 3.0.7 on 2020-09-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO_App', '0008_remove_ngoprofile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoprofile',
            name='description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
