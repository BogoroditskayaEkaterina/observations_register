# Generated by Django 3.1.5 on 2021-08-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations_register', '0008_auto_20210815_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='skin_tumors_in_fam',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
