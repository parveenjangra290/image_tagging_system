from rest_framework import serializers
from image_tag_api.models import Tag, Images


class TagSerializer(serializers.ModelSerializer):
    """
    Tags serializers
    """

    class Meta(object):
        """ Meta information """
        model = Tag
        fields = ('name',)


class ImageSerializer(serializers.ModelSerializer):
    """
    Image serializers
    """

    class Meta(object):
        """ Meta information """
        model = Images
        fields = ('image', 'description', 'tags')


class ImageDetailSerializer(serializers.ModelSerializer):
    """
    Image details serializers
    """

    tags = TagSerializer(read_only=True, many=True)

    class Meta(object):
        """ Meta information """
        model = Images
        fields = ('id', 'tags', 'description', 'image')
