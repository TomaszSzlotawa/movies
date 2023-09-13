from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie, MoreInfo,MovieRating, Actor
from .forms import MovieForm, MoreInfoForm, MovieRatingForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer,MovieSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def all_movies(request):
    all = Movie.objects.all()
    actors = Actor.objects.all()
    return render(request, 'movies.html',{'movies':all,'actors':actors})

@login_required
def new_movie(request):
    form_movie = MovieForm(request.POST or None, request.FILES or None)
    form_more_info = MoreInfoForm(request.POST or None)

    if all((form_movie.is_valid(),form_more_info.is_valid())):
        movie = form_movie.save(commit=False)
        more_info = form_more_info.save()
        movie.more_info = more_info
        movie.save()
        return redirect(all_movies)
    return render(request,'movie_form.html',{'form_movie':form_movie,'form_more_info':form_more_info,'is_new':True})

@login_required
def edit_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    ratings = MovieRating.objects.filter(movie=movie)
    actors = movie.actors.all()
    try:
        more_info = MoreInfo.objects.get(movie=movie.id)
    except MoreInfo.DoesNotExist:
        more_info = None

    form_movie = MovieForm(request.POST or None, request.FILES or None,instance=movie)
    form_more_info = MoreInfoForm(request.POST or None,instance=more_info)
    form_rating = MovieRatingForm(request.POST or None)

    if request.method== 'POST':
        if 'stars' in request.POST:
            rating = form_rating.save(commit=False)
            rating.movie = movie
            rating.save()


    if all((form_movie.is_valid(),form_more_info.is_valid())):
        movie = form_movie.save(commit=False)
        more_info = form_more_info.save()
        movie.more_info = more_info
        movie.save()
        return redirect(all_movies)
    return render(request,'movie_form.html',{'form_movie':form_movie,'form_more_info':form_more_info,'ratings':ratings,'form_rating':form_rating,'actors':actors, 'is_new':False})

@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(all_movies)
    
    return render(request,'confirm.html',{'movie':movie})

@login_required
def rate_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    ratings = MovieRating.objects.filter(movie=movie)
    form_rating = MovieRatingForm(request.POST or None)

    if request.method== 'POST':
        if 'stars' in request.POST:
            rating = form_rating.save(commit=False)
            rating.movie = movie
            rating.save()

    return render(request,'rate_form.html',{'ratings':ratings,'form_rating':form_rating})