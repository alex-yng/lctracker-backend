from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.MakeNote, name="note-list"),
    path('notes/<int:pk>/', views.NoteRetrieveUpdateDestroy.as_view(), name='note-select'),
    path('notes/list/', views.NoteListCreate.as_view(), name='note-list-specific'),
]
