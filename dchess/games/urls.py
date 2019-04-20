from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    # do we need this one?
    path('detail/<int:game_id>', views.detail, name='detail'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<int:game_id>', views.game, name='game'),
    path('<int:game_id>/move/<str:movestring>', views.move, name='move'),
]
