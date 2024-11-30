from django.urls import path,include
from .views import *

urlpatterns = [
    path('', createOrJoinPoll, name = 'create_join_poll'),
    path('ongoing/', poll_list, name = 'ongoing'),
    path('poll/<slug:slug>/', givePoll),
    path('create/', createPollName, name='create'),
    path('create-options/<slug:slug>/', addoptionsToPoll, name='create-options'),
    path('create-options/<slug:slug>/code/', created, name='created'),
]
