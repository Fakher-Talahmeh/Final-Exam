from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('update-location/<int:pk>',views.update),
    path('delete-location/<int:pk>',views.delete),
    path('delete/<int:pk>',views.delete_location),
    path('create-location',views.create),
]