# Generated by Django 4.1.2 on 2022-10-30 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceschool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('members', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=43)),
                ('body', models.TextField()),
            ],
        ),
    ]
