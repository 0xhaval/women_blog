# Generated by Django 2.2.3 on 2019-07-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=40)),
                ('Lname', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Massege', models.TextField()),
            ],
        ),
    ]