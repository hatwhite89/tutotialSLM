# Generated by Django 3.2.7 on 2021-09-29 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialSLMApp', '0005_categoria_sobre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenido',
            name='usuario',
        ),
    ]
