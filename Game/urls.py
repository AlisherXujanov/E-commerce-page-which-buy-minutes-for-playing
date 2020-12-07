from django.urls import path
from .views import *

urlpatterns = [
    path('', GameView.as_view(), name='quiz'),

    path('Vue/', quizInVue.as_view(), name='vue_django'),
    # path('Vue/<str:id>/complete/', TaskComplete.as_view(), name='TaskComplete')
]
