from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ImageWord
from .pagination import DefaultPagination
from .serializers import ImageWordSerializer

# TODO : implement view for getImagesForWords of frontend.

class ImageWordViewSet(ModelViewSet):
    queryset = ImageWord.objects.all()
    serializer_class = ImageWordSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['label']
    search_fields = ['label']
    pagination_class = DefaultPagination


@api_view()
def get_images_for_words(request):
    if request.method == "GET":
        data = request.GET.get("words")
        if data is not None:
            words = [x.strip() for x in data.split(',')]
            queryset = ImageWord.objects 
            
            q = Q(label__icontains=words[0])
            for word in words[1:]:
                q = q | Q(label__icontains=word)
            queryset = queryset.filter(q).all()
            
            serializer = ImageWordSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"Wrong request format."}, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_403_FORBIDDEN)
