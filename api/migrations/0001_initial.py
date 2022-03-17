# Generated by Django 3.2.7 on 2022-03-15 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Nmap",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.basemodel",
                    ),
                ),
                ("target", models.CharField(default="127.0.0.1", max_length=255)),
                ("port_range", models.CharField(default="1-1024", max_length=255, null=True)),
                ("command", models.CharField(default="-v -sS -sV -sC -A -O", max_length=255)),
                ("response", models.JSONField(default=dict, editable=False)),
            ],
            bases=("api.basemodel",),
        ),
    ]
