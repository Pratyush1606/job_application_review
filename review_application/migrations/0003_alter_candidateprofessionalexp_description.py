# Generated by Django 4.1 on 2022-08-26 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review_application", "0002_alter_candidateprofessionalexp_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidateprofessionalexp",
            name="description",
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
