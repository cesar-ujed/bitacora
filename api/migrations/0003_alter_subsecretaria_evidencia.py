# Generated by Django 5.0.1 on 2024-02-12 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_subsecretaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsecretaria',
            name='evidencia',
            field=models.FileField(blank=True, null=True, upload_to='archivos_pdf/'),
        ),
    ]
