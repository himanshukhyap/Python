from django.contrib import admin

from CoinApi.models import AssestManager

@admin.register(AssestManager)
class AssestManagerAdmin(admin.ModelAdmin):
    list_display=['AssestId',
                 'Symbol',
                 'Name',
                  'ThumbImage',
                 'SmallImage','LargeImage']
    
