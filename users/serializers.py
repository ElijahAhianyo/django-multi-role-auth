from rest_framework import serializers
from users.models import User,Roles
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = [
            'id',
            'display'
        ]




class UserSerializer(WritableNestedModelSerializer):
    role = UserRoleSerializer(required=False,many=True)


    class Meta:
        model = User
        fields = [
                'id',
                'email',
                'mobile',
                'role',
                'password'
                ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self,validated_data):

        roles = validated_data.pop('role')
        # validated_data['user_type'] = roles
        user = User.objects.create_user(email=validated_data.pop('email'),password=validated_data.pop('password'),**validated_data)

        role_ids = []
        for role in roles:
            instance = Roles.objects.create(**role)
            role_ids.append(instance.id)
        
        for id in role_ids:
            user.role.add(id)
        
        return user