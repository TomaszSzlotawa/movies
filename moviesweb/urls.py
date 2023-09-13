from django.urls import path
from moviesweb.views import all_movies, new_movie, edit_movie, delete_movie,rate_movie

urlpatterns = [
    path('all/', all_movies, name='all_movies'),
    path('new/', new_movie, name='new_movie'),
    path('edit/<int:id>', edit_movie, name= 'edit_movie'),
    path('delete/<int:id>', delete_movie, name='delete_movie'),
    path('rate/<int:id>', rate_movie, name='rate_movie'),
]