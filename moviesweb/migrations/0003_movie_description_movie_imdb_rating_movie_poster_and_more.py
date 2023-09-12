# Generated by Django 4.2.5 on 2023-09-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesweb', '0002_movie_year_alter_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters'),
        ),
        migrations.AddField(
            model_name='movie',
            name='premiere',
            field=models.DateField(blank=True, null=True),
        ),
    ]
