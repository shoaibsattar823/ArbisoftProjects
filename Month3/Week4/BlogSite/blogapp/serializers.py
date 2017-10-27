from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Blog, Blogger


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class BloggerSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(read_only=True,
                                            slug_field='username')

    class Meta:
        model = Blogger
        fields = ('username', 'first_name', 'last_name', 'email')


class BlogSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Blog
        fields = ('title', 'post', 'published_date', 'blogger')
