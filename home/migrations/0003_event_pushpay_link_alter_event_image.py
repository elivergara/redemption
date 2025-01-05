# Generated by Django 5.1.4 on 2025-01-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="pushpay_link",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="static/images/events/"
            ),
        ),
    ]
