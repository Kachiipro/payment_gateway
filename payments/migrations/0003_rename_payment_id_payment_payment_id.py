# Generated by Django 5.1.2 on 2025-01-23 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_customer_email_payment_customer_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='Payment_id',
            new_name='payment_id',
        ),
    ]