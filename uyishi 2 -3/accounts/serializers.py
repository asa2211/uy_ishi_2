from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone', 'password', 'roles')

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            roles=validated_data.get('roles', 2),
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
