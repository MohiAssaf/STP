# Generated by Django 4.0.3 on 2022-04-26 22:16

import ShareTheWorld.validators.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_owner', models.CharField(max_length=15, validators=[ShareTheWorld.validators.validators.validate_only_letters])),
                ('comment_body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_of_place', models.URLField(verbose_name='Flag URL')),
                ('name_of_place', models.CharField(max_length=20, verbose_name='Place visiting')),
                ('budget', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('note', models.TextField(verbose_name='Notes')),
                ('date_going', models.DateField(verbose_name='Date visiting')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), ShareTheWorld.validators.validators.validate_only_letters])),
                ('photo', models.URLField()),
                ('place_visited', models.CharField(max_length=20)),
                ('date_visited', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
