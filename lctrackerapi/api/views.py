from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.
# create a view that lists (using restframework) all note objects using the note serializer
class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    def delete(self, request, *args, **kwargs):
        Note.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk' # primary key
    
class NoteListView(APIView):
    def get(self, request, format=None):
        title = request.query_params.get('title', None)
        
        if title:
            notes = Note.objects.filter(title_icontains=title)
        else:
            notes = Note.objects.all()
            
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def MakeNote(request):
    if request.method == 'POST':
        print(request.data)
        Note.objects.create(title=request.data['title'], content=request.data['content'])
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Note.objects.all()