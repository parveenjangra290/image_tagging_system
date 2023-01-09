from datetime import datetime
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from image_tag_api.api.serializers import (TagSerializer, ImageSerializer, ImageDetailSerializer)
from image_tag_api.models import Images

class TagAPIViewSet(viewsets.GenericViewSet):
    """
    Create Tag API view set
    """

    def get_queryset(self):
        return

    @action(
        detail=False, methods=['POST'], serializer_class=TagSerializer,
        permission_classes=[IsAuthenticated], url_path='tag', url_name='tag'
    )
    def tags(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tag Created Successfully'}, status=status.HTTP_200_OK)
        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ImageAPIViewSet(viewsets.GenericViewSet):
    """
    Create Image API view set
    """
    
    def get_queryset(self):
        return
    
    @action(
        detail=False, methods=['POST'], serializer_class=ImageSerializer,
        permission_classes=[IsAuthenticated], url_path='image', url_name='image'
    )
    def create_image(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(ImageDetailSerializer(instance=data).data, status=status.HTTP_200_OK)
        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(
        detail=False, methods=['PUT'], serializer_class=ImageSerializer,
        permission_classes=[IsAuthenticated], url_path='image/update/(?P<image_pk>[^/.]+)'
    )
    def edit_image(self, request, pk=None, image_pk=None):
        img = Images.objects.filter(id=image_pk)
        serializer = self.get_serializer(instance=img[0], data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(ImageDetailSerializer(instance=data).data, status=status.HTTP_200_OK)
        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(
        detail=False, methods=['GET'], serializer_class=ImageDetailSerializer,
        permission_classes=[IsAuthenticated], url_path='images/search'
    )
    def search_images(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date', False)
        end_date = request.GET.get('end_date', False)
        if start_date and end_date:
            start_date = timezone.make_aware(datetime.strptime(start_date + ' 00:00:00', "%Y-%m-%d %H:%M:%S"), timezone.get_default_timezone())
            end_date = timezone.make_aware(datetime.strptime(end_date + ' 23:59:59', "%Y-%m-%d %H:%M:%S"), timezone.get_default_timezone())
        if start_date and end_date:
            img = Images.objects.filter(created_at__range=[start_date, end_date])
            if img:
                return Response({'data':ImageDetailSerializer(instance=img, many=True).data}, status=status.HTTP_200_OK)
            return Response(data={'message': "Data Not Found"}, status=status.HTTP_200_OK)
        else:
            return Response(data={'error': "Please supply start date or end date as query parameter"}, status=status.HTTP_400_BAD_REQUEST)
