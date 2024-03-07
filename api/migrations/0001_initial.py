# Generated by Django 3.2.24 on 2024-02-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('unit_of_measure', models.CharField(choices=[('ltr', 'Liter'), ('kg', 'Kilogram'), ('pcs', 'Pieces')], max_length=10)),
            ],
        ),
    ]