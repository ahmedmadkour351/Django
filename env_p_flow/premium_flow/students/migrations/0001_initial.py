# Generated by Django 4.0.4 on 2022-05-22 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.IntegerField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('mobil', models.CharField(max_length=15)),
                ('mail', models.EmailField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
