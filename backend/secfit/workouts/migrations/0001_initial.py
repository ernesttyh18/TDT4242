# Generated by Django 3.1 on 2020-08-21 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import workouts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("unit", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Workout",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("date", models.DateTimeField()),
                ("notes", models.TextField()),
                (
                    "visibility",
                    models.CharField(
                        choices=[("PU", "Public"), ("CO", "Coach"), ("PR", "Private")],
                        default="CO",
                        max_length=2,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workouts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
        migrations.CreateModel(
            name="WorkoutFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(upload_to=workouts.models.workout_directory_path),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "workout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="workouts.workout",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExerciseInstance",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sets", models.IntegerField()),
                ("number", models.IntegerField()),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="instances",
                        to="workouts.exercise",
                    ),
                ),
                (
                    "workout",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exercise_instances",
                        to="workouts.workout",
                    ),
                ),
            ],
        ),
    ]
