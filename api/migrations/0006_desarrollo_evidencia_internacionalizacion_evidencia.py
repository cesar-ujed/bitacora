# Generated by Django 5.0.1 on 2024-02-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_servicios_evidencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='desarrollo',
            name='evidencia',
            field=models.FileField(blank=True, null=True, upload_to='archivos_pdf/'),
        ),
        migrations.AddField(
            model_name='internacionalizacion',
            name='evidencia',
            field=models.FileField(blank=True, null=True, upload_to='archivos_pdf/'),
        ),
    ]
