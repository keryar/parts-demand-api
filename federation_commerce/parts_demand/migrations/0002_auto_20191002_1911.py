# Generated by Django 2.2.5 on 2019-10-02 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts_demand', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partsdemand',
            old_name='announcer',
            new_name='owner',
        ),
    ]
