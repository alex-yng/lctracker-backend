from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.decorators import api_view

# Create your views here.
class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk' # primary key

# CRUD operations
# Create a note
@api_view(['POST'])
def MakeNote(request):
    if Note.objects.filter(title=request.data['title']).exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    Note.objects.create(title=request.data['title'], content=request.data['content'])
    return Response(status=status.HTTP_201_CREATED)

# Get all notes
@api_view(['GET'])
def GetNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# Get a specific note
@api_view(['GET'])
def GetNote(request, probID):
    note = Note.objects.get(title=probID)
    serializer = NoteSerializer(note)
    return Response(serializer.data)

# Update a note
@api_view(['PUT'])
def UpdateNote(request, probID):
    if probID:
        note = Note.objects.get(title=probID)
        note.content = request.data['content']
        note.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Delete a note
@api_view(['DELETE'])
def DeleteNote(request, probID):
    if probID:
        note = Note.objects.get(title=probID)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    