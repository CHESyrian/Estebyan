# Generated by Django 3.0.6 on 2020-11-29 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20201129_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='Questionnairs',
            new_name='Questionnaires',
        ),
    ]
