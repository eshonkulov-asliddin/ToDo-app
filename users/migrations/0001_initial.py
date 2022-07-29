# Generated by Django 4.0.6 on 2022-07-21 15:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]