# Generated by Django 3.0.6 on 2020-11-05 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('ID_User', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('FirstName', models.CharField(max_length=32, null=True)),
                ('LastName', models.CharField(max_length=32, null=True)),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
