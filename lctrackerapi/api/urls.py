from django.urls import path
from . import views

urlpatterns = [
    path('crud/<int:pk>/', views.NoteRetrieveUpdateDestroy.as_view(), name='note-crud'),
    
    # Custom CRUD operations
    path('notes/create/',views.MakeNote, name='note-create'),
    path('notes/',views.GetNotes, name='note-get'),
    path('notes/<str:probID>/', views.GetNote, name='note-get-specific'),
    path('notes/<str:probID>/', views.UpdateNote, name='note-update'),
    path('notes/<str:probID>/', views.DeleteNote, name='note-delete'),
]
