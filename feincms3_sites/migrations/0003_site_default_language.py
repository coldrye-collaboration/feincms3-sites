# Generated by Django 2.0.4 on 2018-04-19 07:13

from django.conf import global_settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("feincms3_sites", "0002_site_is_managed_re")]

    operations = [
        migrations.AddField(
            model_name="site",
            name="default_language",
            field=models.CharField(
                blank=True,
                choices=global_settings.LANGUAGES,
                help_text="The default language will be overridden by more specific settings such as the language of individual pages.",
                max_length=10,
                verbose_name="default language",
            ),
        )
    ]
