# Generated by Django 4.1.3 on 2022-11-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgg', models.ImageField(upload_to='pics')),
                ('nameg', models.CharField(max_length=250)),
                ('descg', models.TextField()),
            ],
        ),
    ]
