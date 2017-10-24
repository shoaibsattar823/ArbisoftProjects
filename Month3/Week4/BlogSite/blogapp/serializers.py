from rest_framework import serializers

from .models import Blog, Blogger

# tempBloggers = []


class BloggerSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(read_only=True,
                                            slug_field='username')

    class Meta:
        model = Blogger
        fields = ('username', 'first_name', 'last_name', 'email')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    # blogger = serializers.SlugRelatedField(read_only=True,
    #                                       slug_field='first_name')
    # blogger = BloggerSerializer()
    # bloggers = serializers.SerializerMethodField('get_blogger_options')

    class Meta:
        model = Blog
        fields = ('title', 'post', 'published_date', 'blogger')

    # def get_blogger_options(self, obj):
    #     global tempBloggers
    #     if (obj.blogger.first_name not in tempBloggers):
    #         tempBloggers.append(obj.blogger.first_name)
    #     print tempBloggers
    #     return tempBloggers
