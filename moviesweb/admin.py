from django.contrib import admin
from .models import Movie, MoreInfo, MovieRating, Actor

# Register your models here.
#admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields = ['title','description', 'year']
    #exclude = ['title']
    list_display = ['title', 'year']
    list_filter = ['year','imdb_rating']
    search_fields = ('title','description')

admin.site.register(MoreInfo)
admin.site.register(MovieRating)
admin.site.register(Actor)

