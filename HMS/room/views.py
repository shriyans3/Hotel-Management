from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Room, RoomType
from .serializers import RoomSerializer, RoomTypeSerializer

# Views for Rooms
@api_view(['GET', 'POST'])
def room_list(request):
    """
    List all rooms or create a new room.
    """
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def room_detail(request, room_id):
    """
    Retrieve, update or delete a room instance.
    """
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views for Room Types
@api_view(['GET'])
def room_type_list(request):
    """
    List all room types.
    """
    room_types = RoomType.objects.all()
    serializer = RoomTypeSerializer(room_types, many=True)
    return Response(serializer.data)
