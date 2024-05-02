from rest_framework import serializers
from follower.models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = ReadOnlyField(source='owner.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_at', 'followed', 'followed_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})

