# Generated by Django 4.2.3 on 2023-10-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("volunteer", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="scoreeventdata",
            name="desc",
        ),
        migrations.AddField(
            model_name="studentscoredata",
            name="date_of_activity",
            field=models.CharField(
                default="2023", max_length=200, verbose_name="Date Data"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="studentscoredata",
            name="desc",
            field=models.CharField(
                default="2023", max_length=200, verbose_name="Description"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="scoreeventdata",
            name="point",
            field=models.FloatField(),
        ),
    ]
