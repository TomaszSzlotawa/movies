# Generated by Django 4.2.5 on 2023-09-12 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviesweb', '0004_moreinfo_movie_more_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Drama'), (1, 'Horror'), (4, 'Sci-fi'), (3, 'Comedia'), (0, 'Other')], default=0),
        ),
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, default='')),
                ('stars', models.PositiveSmallIntegerField(default=5)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesweb.movie')),
            ],
        ),
    ]
