# Generated by Django 4.1.2 on 2022-11-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('isActivate', models.BooleanField(default=True)),
                ('password', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
