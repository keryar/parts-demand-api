# Generated by Django 2.2.5 on 2019-10-03 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_demand', '0004_auto_20191003_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsdemand',
            name='status',
            field=models.CharField(choices=[('Finalizado', 'Finalizado'), ('Não Finalizado', 'Não Finalizado')], default='Não Finalizado', max_length=500),
        ),
    ]
