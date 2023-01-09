from django.db import models


class Tag(models.Model):
    """
    Model for Tags
    """

    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta(object):
        """ Meta information """
        verbose_name_plural = 'Tags'


class Images(models.Model):
    """
    Model for Images
    """

    image = models.ImageField(upload_to='images', null=True, blank=True, max_length=None)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.image.name}'

    @property
    def image_name(self):
        """ Return file name """
        if self.image:
            return "{0}".format(self.image.name)
    
    @property
    def tag_name(self):
        if self.tags:
            return "{0}".format(self.tags.name)

    class Meta(object):
        """ Meta information """
        verbose_name_plural = 'Images'