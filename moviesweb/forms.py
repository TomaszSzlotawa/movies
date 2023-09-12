from django.forms import ModelForm
from .models import Movie, MoreInfo, MovieRating

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title','year','description','premiere','imdb_rating','poster']

class MoreInfoForm(ModelForm):
    class Meta:
        model = MoreInfo
        fields = ['duration','genre']

class MovieRatingForm(ModelForm):
    class Meta:
        model = MovieRating
        fields = ['stars','review']