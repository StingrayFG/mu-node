from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes


from .serializers import FolderSerializer
from .models import Folder


class FolderView(APIView):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

    @api_view(('GET',))
    def get_uuid(request, uuid):
        try:            
            d = Folder.objects.get(uuid = uuid)
            serializer = FolderSerializer(d)
            return Response(data = serializer.data)
        except Folder.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
