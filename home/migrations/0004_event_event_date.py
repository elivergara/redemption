# Generated by Django 5.1.4 on 2025-01-10 02:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_event_pushpay_link_alter_event_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="event_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]