# Generated by Django 5.0.3 on 2024-03-06 01:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0014_alter_accountlookup_language"),
        ("stats", "0004_accountstats"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AccountStats",
            new_name="DailyAccount",
        ),
    ]
