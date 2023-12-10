from .views import *
from django.urls import path,include
urlpatterns = [
    path('start_interview', start_interview.as_view()),
    path('get_next_question', get_next_question.as_view()),
    path('end_interview', end_interview.as_view()),
    

]