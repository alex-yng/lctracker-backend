from django.urls import path
from . import views

urlpatterns = [
    path('crud/<int:pk>/', views.NoteRetrieveUpdateDestroy.as_view(), name='note-crud'),
    path('note/create/',views.MakeNote, name='note-create')
]
