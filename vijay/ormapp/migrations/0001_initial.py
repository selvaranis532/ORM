# Generated by Django 5.1.2 on 2024-10-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_loan',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('Aadharno', models.IntegerField(primary_key='Aadharno', serialize=False)),
                ('Accountno', models.IntegerField()),
                ('Address', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]