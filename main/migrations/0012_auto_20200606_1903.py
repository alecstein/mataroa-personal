# Generated by Django 3.0.7 on 2020-06-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_auto_20200606_1903"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="custom_domain",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]