# Create your models here.
import json
from django import forms
from django.db import models
from django.db.models.fields import AutoField, CharField, DateField, DateTimeField, FloatField, IntegerField, URLField
from django.db.models.fields.related import ForeignKey
from rest_framework import viewsets

class AssestManager(models.Model):
   
    AssestId = models.CharField(max_length=250,primary_key=True)
    Symbol = models.CharField(blank=True ,max_length=250)
    Name = models.CharField(blank=True ,max_length=250)
    ThumbImage = models.CharField(blank=True ,max_length=250)
    SmallImage = models.CharField(blank=True,max_length=250 )
    LargeImage = models.CharField(blank=True,max_length=250 )

class Social_data(models.Model):
    facebook_likes:FloatField(max_length=250, blank=False)
    twitter_followers:FloatField(max_length=250, blank=False)
    reddit_average_posts_48h:FloatField(max_length=250, blank=False)
    reddit_average_comments_48h:FloatField(max_length=250, blank=False)

class AssestDetail(models.Model):
     
     AssestId = models.CharField(max_length=250,)
     HashingAlgorithm= CharField(max_length=250, blank=False)
     Categories = CharField(max_length=250, blank=True)
     Localization = CharField(max_length=250, blank=False)
     Description = CharField(max_length=250, blank=False)
     Homepage = URLField(max_length=250, blank=False)
     Genesis_date = DateField(max_length=250, blank=False)
     sentiment_votes_up_percentage = CharField(max_length=250, blank=False)
     sentiment_votes_down_percentage = CharField(max_length=250, blank=False)
     market_cap_rank = IntegerField( blank=False)
     coingecko_rank = FloatField(max_length=250, blank=False)
     coingecko_score = FloatField(max_length=250, blank=False)
     developer_score = FloatField(max_length=250, blank=False)
     community_score = FloatField(max_length=250, blank=False)
     liquidity_score = FloatField(max_length=250, blank=False)
     public_interest_score = FloatField(max_length=250, blank=False)
     Last_Updated = DateTimeField(max_length=250, blank=False)
     
       

  #"coingecko_rank": 2413,
  #"coingecko_score": 14.566,
  #"developer_score": 44.12,
  #"community_score": 15.164,
  #"liquidity_score": 1,
  #"public_interest_score": 0,
  #"Last_Updated": "2022-07-25T04:57:40.002Z",
  #"Social_data": {
  #  "facebook_likes": null,
  #  "twitter_followers": 366,
  #  "reddit_average_posts_48h": 0,
  #  "reddit_average_comments_48h": 0,
  #  "reddit_subscribers": 28,
  #  "reddit_accounts_active_48h": 6,
  #  "telegram_channel_user_count": 186
  #}
     
  

