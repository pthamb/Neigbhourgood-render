# Generated by Django 5.0 on 2023-12-15 12:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_rename_erands_user_coffeetea_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("name", models.CharField(max_length=200)),
                ("age", models.IntegerField()),
                ("email", models.CharField(max_length=200)),
                ("zipCode", models.IntegerField()),
                ("mobile", models.CharField(max_length=120, unique=True)),
                ("walking", models.CharField(max_length=200)),
                ("running", models.CharField(max_length=200)),
                ("gardening", models.CharField(max_length=200, null=True)),
                ("swimming", models.CharField(max_length=200)),
                ("coffeeTea", models.CharField(max_length=200, null=True)),
                ("foodGathering", models.CharField(max_length=200, null=True)),
                ("televisionSports", models.CharField(max_length=200, null=True)),
                ("movies", models.CharField(max_length=200, null=True)),
                ("shopping", models.CharField(max_length=200, null=True)),
                ("happyHours", models.CharField(max_length=200, null=True)),
                ("errands", models.CharField(max_length=200, null=True)),
                ("rides", models.CharField(max_length=200, null=True)),
                ("childcare", models.CharField(max_length=200, null=True)),
                ("eldercare", models.CharField(max_length=200, null=True)),
                ("petcare", models.CharField(max_length=200, null=True)),
                ("tutoring", models.CharField(max_length=200, null=True)),
                ("repairAdvice", models.CharField(max_length=200, null=True)),
                ("otherAdvice", models.CharField(max_length=200, null=True)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("sharePreference", models.CharField(max_length=200)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
