# Generated by Django 4.2.5 on 2023-09-12 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviesweb', '0003_movie_description_movie_imdb_rating_movie_poster_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(default=0)),
                ('genre', models.PositiveSmallIntegerField(choices=[(4, 'Sci-fi'), (0, 'Other'), (2, 'Drama'), (1, 'Horror'), (3, 'Comedia')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='more_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moviesweb.moreinfo'),
        ),
    ]
