# Generated by Django 3.1.3 on 2020-11-15 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
