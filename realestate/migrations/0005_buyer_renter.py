# Generated by Django 5.0.4 on 2024-04-25 15:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0004_remove_rent_agent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.IntegerField(default=1)),
                ('phone', models.CharField(max_length=11)),
                ('location', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('sell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.sell')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('location', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realestate.rent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
