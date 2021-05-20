from rest_framework import generics
from .serializers import NewsDetailSerializer, NewsListSerializer
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsDetailSerializer
    permission_classes = (IsAdminUser, )
    authentication_classes = (TokenAuthentication, )


class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
