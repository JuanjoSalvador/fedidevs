# Generated by Django 5.0 on 2024-01-04 02:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("confs", "0005_dotnetconfaccount_dotnetconfpost_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Conference",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("location", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
            ],
        ),
    ]