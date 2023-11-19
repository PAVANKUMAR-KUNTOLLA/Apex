# Generated by Django 4.2.3 on 2023-10-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_services', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tax_filings',
            field=models.ManyToManyField(related_name='filings', to='tax_services.taxfiling'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]