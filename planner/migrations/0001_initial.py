# Generated by Django 5.1.5 on 2025-01-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlannerEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("where", models.CharField(blank=True, max_length=200, null=True)),
                ("when", models.DateTimeField()),
                ("duration", models.DurationField(blank=True, null=True)),
                (
                    "cost",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                ("contact", models.CharField(max_length=200)),
                ("category", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Optional one-line description", null=True
                    ),
                ),
            ],
        ),
    ]
