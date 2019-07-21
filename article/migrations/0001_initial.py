# Generated by Django 2.2.3 on 2019-07-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article_auther', models.CharField(max_length=100)),
            ],
        ),
    ]