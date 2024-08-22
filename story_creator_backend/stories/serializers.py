# stories/serializers.py
from rest_framework import serializers
from .models import Story, Contribution
from django.conf import settings

class ContributionSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    

    class Meta:
        model = Contribution
        fields = ['id', 'username', 'text', 'created_at', ]

    
class StorySerializer(serializers.ModelSerializer):
    contributions = ContributionSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ['id', 'title', 'created_at', 'completed', 'image', 'contributions', 'first_sentence']

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return f"{settings.MEDIA_URL}{obj.image}"
        return None

    def validate_image(self, value):
        if value:
            if value.size > 1024 * 1024 * 5:  # 5 MB limit
                raise serializers.ValidationError("Image file too large ( > 5 MB )")
            if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                raise serializers.ValidationError("Unsupported file extension")
        return value

