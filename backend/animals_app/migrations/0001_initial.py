# Generated by Django 5.1.4 on 2024-12-15 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('average_age', models.IntegerField()),
                ('feed', models.CharField(max_length=255)),
                ('bathe', models.CharField(max_length=255)),
                ('temperature', models.CharField(max_length=255)),
                ('yields', models.CharField(max_length=255)),
            ],
        ),
    ]
