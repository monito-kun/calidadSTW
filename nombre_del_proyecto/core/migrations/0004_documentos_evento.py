# Generated by Django 5.0.6 on 2024-10-20 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_documentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos',
            name='evento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.evento'),
            preserve_default=False,
        ),
    ]
