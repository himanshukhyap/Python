from rest_framework import serializers 
from User.models import Album, Musician

 
class MusicianSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Musician
        fields = ('first_name',
                  'last_name',
                  'instrument')


class AlbumSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Album
        fields = ('artist',
                  'name',
                  'release_date','num_stars')

   
