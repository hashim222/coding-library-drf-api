from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        'Message': 'Welcome to my Coding Library drf API!'
    })
