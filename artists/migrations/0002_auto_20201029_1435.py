# Generated by Django 3.1.2 on 2020-10-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='artists',
            field=models.ManyToManyField(related_name='tags', to='artists.Artist'),
        ),
    ]
