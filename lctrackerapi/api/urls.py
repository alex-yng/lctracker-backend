from django.urls import path
from . import views

urlpatterns = [
    path('crud/<int:pk>/', views.NoteRetrieveUpdateDestroy.as_view(), name='note-crud'),
    path('notes/create/',views.MakeNote, name='note-create'),
    path('notes/',views.GetNotes, name='note-get'),
    path('notes/<str:probID>/delete/', views.DeleteNote, name='note-delete'),
]
