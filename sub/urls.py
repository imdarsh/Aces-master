from django.urls import path
from . import views

urlpatterns = [
    path('setexam',views.setexam,name='setexam'),
    path('ffem',views.ffem,name='ffem'),
    path('exam',views.exam,name='exam'),
    path('start_exam/<str:subject>',views.start_exam,name='start_exam')
]