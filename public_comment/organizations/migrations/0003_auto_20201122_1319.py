# Generated by Django 3.1.3 on 2020-11-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("organizations", "0002_auto_20201006_2338")]

    operations = [
        migrations.RemoveField(model_name="organization", name="url_short_name"),
        migrations.AddField(
            model_name="organization",
            name="slug",
            field=models.SlugField(
                default="blank",
                editable=False,
                help_text="Something short to use in the URL of this org's documents (eg. ACLU). Cannot be changed.",
                max_length=30,
            ),
            preserve_default=False,
        ),
    ]
