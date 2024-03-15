from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_info(request):
    """
    Return information about the API.
    """
    info = {
        'name': 'Hotel Room Management API',
        'version': '1.0',
        'description': 'API for managing hotel rooms and bookings.',
        # Add more information as needed
    }
    return Response(info)
