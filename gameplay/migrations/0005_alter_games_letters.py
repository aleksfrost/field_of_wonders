# Generated by Django 5.2 on 2025-05-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0004_alter_categories_categorie_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='letters',
            field=models.CharField(blank=True, max_length=33, null=True),
        ),
    ]
