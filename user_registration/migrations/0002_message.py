# Generated by Django 5.0 on 2024-01-27 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('post', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('replies', models.ManyToManyField(blank=True, to='user_registration.message')),
                ('repliesTo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_registration.message')),
            ],
        ),
    ]
