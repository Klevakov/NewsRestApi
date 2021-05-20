from rest_framework import serializers
from .models import News


class NewsDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = ('pub_date', 'title', 'news_text', 'user')


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('pub_date', 'title')
