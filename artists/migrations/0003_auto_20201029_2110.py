# Generated by Django 3.1.2 on 2020-10-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20201029_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('artists', models.ManyToManyField(to='artists.Artist')),
            ],
        ),
        migrations.RenameModel(
            old_name='States',
            new_name='State',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.AddField(
            model_name='artist',
            name='tags',
            field=models.ManyToManyField(to='artists.Tag'),
        ),
    ]
