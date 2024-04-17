from django.urls import path
from . import views

urlpatterns = [
    path('crud/<int:pk>/', views.NoteRetrieveUpdateDestroy.as_view(), name='note-crud'),
    
    # Custom CRUD operations
    path('notes/',views.GetCreateNotes, name='note-get-create-notes'),
    path('notes/<str:probID>/', views.ModifyNote, name='note-modify'),
]
