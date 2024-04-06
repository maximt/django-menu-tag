# Generated by Django 5.0.4 on 2024-04-23 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=128, unique=True)),
                ("title", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
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
                ("title", models.CharField(max_length=256)),
                ("depth", models.IntegerField(default=0)),
                (
                    "mpath",
                    models.CharField(blank=True, default="", max_length=512, null=True),
                ),
                ("url", models.URLField(blank=True, max_length=2048, null=True)),
                ("named_url", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "named_url_kwargs",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mymenu.menu"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="mymenu.menuitem",
                    ),
                ),
            ],
            options={
                "ordering": ["mpath"],
            },
        ),
    ]