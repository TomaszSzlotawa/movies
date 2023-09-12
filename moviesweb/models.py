from django.db import models

class MoreInfo(models.Model):
        Genre = {
            (0,'Other'),
            (1,'Horror'),
            (2,'Drama'),
            (3,'Comedia'),
            (4,'Sci-fi')
        }
        duration = models.PositiveSmallIntegerField(default=0)
        genre = models.PositiveSmallIntegerField(default=0, choices=Genre)

class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    more_info = models.OneToOneField(MoreInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_with_year()
    
    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)
    
class MovieRating(models.Model):
     review = models.TextField(default='', blank=True)
     stars = models.PositiveSmallIntegerField(default = 5)
     movie = models.ForeignKey(Movie,on_delete=models.CASCADE)


class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    movies = models.ManyToManyField(Movie,related_name='actors')

    def __str__(self):
         return (self.name + ' '+ self.surname)



