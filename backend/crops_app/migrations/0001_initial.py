# Generated by Django 5.1.4 on 2024-12-15 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('average_yield', models.CharField(max_length=255)),
                ('growth_time', models.CharField(max_length=255)),
                ('soil', models.CharField(max_length=255)),
                ('waterring', models.CharField(max_length=255)),
                ('health_benefits', models.CharField(max_length=255)),
            ],
        ),
    ]