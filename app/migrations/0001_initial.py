# Generated by Django 4.1.7 on 2023-03-05 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('School', models.CharField(max_length=100)),
                ('sec', models.IntegerField()),
            ],
        ),
    ]