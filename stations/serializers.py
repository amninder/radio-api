from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from stations.models import Station





class StationSerializer(serializers.Serializer):
    pk 		= serializers.Field()  # Note: `Field` is an untyped read-only field.
    name 	= serializers.CharField(required=False,
    max_length=100)
    lat 	= serializers.CharField(required=False,
    max_length=100)
    lng 	= serializers.CharField(required=False,
    max_length=100)
    url 	= serializers.CharField(required=False,
    max_length=100)
    school  = serializers.CharField(required=False,
    max_length=100)
    state  = serializers.CharField(required=False,
    max_length=100)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.lat = attrs.get('lat', instance.lat)
            instance.lng = attrs.get('lng', instance.lng)
            instance.url = attrs.get('url', instance.url)
            instance.school = attrs.get('school', instance.url)
            instance.state = attrs.get('state', instance.url)
            return instance

            # Create new instance
            return Snippet(**attrs)



            """
            name 			= models.CharField(('name'), max_length=255)
            lat 			= models.CharField(('lat'), max_length=255)
            lng 			= models.CharField(('lng'), max_length=255)
            url 			= models.CharField(('url'), max_length=255)

            """
