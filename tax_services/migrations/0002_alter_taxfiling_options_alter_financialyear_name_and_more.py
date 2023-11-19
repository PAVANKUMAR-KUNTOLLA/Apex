# Generated by Django 4.2.3 on 2023-10-13 14:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tax_services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxfiling',
            options={'verbose_name': 'Tax Filing'},
        ),
        migrations.AlterField(
            model_name='financialyear',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='taxfiling',
            unique_together={('user', 'year')},
        ),
    ]
