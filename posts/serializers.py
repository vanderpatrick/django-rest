from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializer.ReadOnlyField(source='owner.username')
    profile_id = serializer.ReadOnlyField(source='owner.profile.id')
    profile_image = serializer.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image Width larger than 4096px"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "image height larger than 4096px"
            )
        return value

    def get_is_owner(self, Obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'image_filter',
            'title', 'content', 'image']
