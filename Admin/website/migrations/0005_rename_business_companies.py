# Generated by Django 5.0 on 2024-01-25 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0004_business"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Business",
            new_name="Companies",
        ),
    ]
