# Generated by Django 5.0.2 on 2024-08-13 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_alter_noticia_textonoticia1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='imagenEncabezado',
            new_name='imagenPreview',
        ),
    ]
