# Generated by Django 4.0.6 on 2022-07-28 15:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='contenido',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='posteos'),
        ),
    ]
