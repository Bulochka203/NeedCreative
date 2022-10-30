# Generated by Django 4.1.2 on 2022-10-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coin', models.CharField(max_length=100, null=True)),
                ('performed', models.BooleanField()),
                ('icon', models.CharField(choices=[(models.CharField(max_length=100, null=True), 'coin')], max_length=10, null=True)),
                ('text', models.CharField(max_length=255)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(default=1, help_text='Введите id профиля', max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='Введите имя пользователя', max_length=30)),
                ('last_name', models.CharField(help_text='Введите фамилию пользователя', max_length=30)),
                ('photo', models.ImageField(help_text='Загрузите фотографию пользователя', upload_to='profiles/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('balance', models.CharField(help_text='Введите баланс DanceCoin', max_length=6)),
                ('category', models.CharField(choices=[('DD media', 'DDM'), ('Mentor', 'M'), ('Dancer', 'D'), ('Team Leader', 'TL'), ('Trainer', 'T'), ('Admin', 'Adm')], default='Adm', help_text='Выберете категорию пользователя', max_length=20)),
                ('rang', models.CharField(choices=[('junior', 'jun'), ('middle', 'mid'), ('senior', 'sen'), ('vice president', 'VP')], default='sen', help_text='Выберете ранг пользователя', max_length=20)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'ordering': ['-created_at', '-first_name', '-last_name'],
            },
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('energy', models.IntegerField(default=0, null=True)),
                ('sun', models.IntegerField(default=0, null=True)),
                ('water', models.IntegerField(default=0, null=True)),
                ('timer', models.TimeField(auto_now=True)),
            ],
        ),
    ]