# Generated by Django 3.2.13 on 2022-12-07 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20221207_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnostique_lesion_organe',
            old_name='organe',
            new_name='nom_organe',
        ),
    ]
