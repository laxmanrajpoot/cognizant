# Generated by Django 4.1 on 2023-11-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_leave"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leave",
            name="Emp_num",
            field=models.IntegerField(unique=True),
        ),
    ]