# Generated by Django 4.1.4 on 2022-12-11 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exercise", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="reqs",
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="video",
            name="videofile",
            field=models.FileField(null=True, upload_to="", verbose_name=""),
        ),
    ]