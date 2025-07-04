# Generated by Django 5.1.1 on 2025-06-22 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('match_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
