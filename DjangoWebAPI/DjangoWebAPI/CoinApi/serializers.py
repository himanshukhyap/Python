
from rest_framework import serializers 
from CoinApi.models import AssestManager
 
 
class AssestManagerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AssestManager
        fields = ('AssestId',
                  'Symbol',
                  'Name',
                  'ThumbImage',
                  'SmallImage','LargeImage'           )

         