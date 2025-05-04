
from django.db.models import fields
from rest_framework import serializers 
from CoinApi.models import AssestDetail, AssestManager, Social_data
 
 
class AssestManagerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AssestManager
        fields = "__all__"
        #fields = ('AssestId',
        #          'Symbol',
        #          'Name',
        #          'ThumbImage',
        #          'SmallImage','LargeImage'       )

     
                 
class AssestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssestDetail
        fields = []
        #class Meta:
        #     model = AssestDetail
        #     fields = "__all__"
        #fields = ('AssestId','HashingAlgorithm','Categories',"Localization","Description","Homepage",
        #"Genesis_date", "sentiment_votes_up_percentage","sentiment_votes_down_percentage",
        #"market_cap_rank"
                  
        #          )