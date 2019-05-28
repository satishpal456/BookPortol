# Generated by Django 2.0.13 on 2019-03-27 15:00

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0010_libraryprofile_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryaddbook',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True),
        ),
    ]
