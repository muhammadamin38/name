# Generated by Django 3.1 on 2022-11-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=255)),
                ('rangi', models.TextField()),
                ('turi', models.DateTimeField(auto_now_add=True)),
                ('rasmi', models.CharField(max_length=255)),
            ],
        ),
    ]