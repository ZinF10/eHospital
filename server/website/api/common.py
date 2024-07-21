from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Tag, User


class BaseSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = None
        fields = ['slug']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'avatar', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        group, _ = Group.objects.get_or_create(name="Patient")
        user.groups.add(group)
        user.role = group
        user.save()
        return user


class InforSerializer(BaseSerializer):
    user = UserSerializer(required=True)
    
    class Meta:
        model = BaseSerializer.Meta.model
        fields = BaseSerializer.Meta.fields + ["user"]
    
    
class InforDetailsSerializer(InforSerializer):
    class Meta:
        model = InforSerializer.Meta.model
        fields = InforSerializer.Meta.fields + ["phone"]
   
       
class TagSerializer(BaseSerializer):
    class Meta:
        model = Tag
        fields = BaseSerializer.Meta.fields + ["name"]
         
        
class ItemSerializer(BaseSerializer):
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = BaseSerializer.Meta.model
        fields = BaseSerializer.Meta.fields + ["tags"]