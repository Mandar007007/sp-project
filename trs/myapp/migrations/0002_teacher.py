# Generated by Django 4.1.5 on 2023-03-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
