from rest_framework import serializers

from .models import Blog, Blogger


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    blogger = serializers.SlugRelatedField(read_only=True,
                                           slug_field='first_name')

    class Meta:
        model = Blog
        fields = ('title', 'post', 'published_date', 'blogger')


class BloggerSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(read_only=True,
                                            slug_field='username')

    class Meta:
        model = Blogger
        fields = ('username', 'first_name', 'last_name', 'email')
