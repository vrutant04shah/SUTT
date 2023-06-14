# Generated by Django 4.1.7 on 2023-06-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_prescriptions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                (
                    "doctor",
                    models.CharField(
                        choices=[
                            ("ENT", "ENT"),
                            ("Cardiologist", "Cardiologist"),
                            ("Neurologist", "Neurologist"),
                            ("Oncologist", "Oncologist"),
                            ("Orthopedia", "Orthopedia"),
                            ("Pediatrician", "Pediatrician"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]