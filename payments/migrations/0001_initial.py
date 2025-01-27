# Generated by Django 5.1.2 on 2025-01-23 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('Customer_email', models.EmailField(max_length=254)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Payment_id', models.CharField(max_length=255)),
                ('status', models.CharField(default='pending', max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
