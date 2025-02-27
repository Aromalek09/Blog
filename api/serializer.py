from rest_framework import serializers
from .models import *



class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description','cost'] 

class ProjectDetailSerializer(serializers.ModelSerializer):
    custom_field = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    def get_custom_field(self, obj):
        return f"Custom Info: {obj.name} - {obj.cost}"


class ProjectCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    
    def validate_name(self, value):
    
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError("A project with this name already exists.")
        return value
        
    def save(self):

        name = self.validated_data['name']
        description = self.validated_data['description']
        cost = self.validated_data['cost']


        project = Project.objects.create(
            name=name,
            description=description,
            cost=cost
        )
    
        return project
        
        
class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'cost']






        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Blog
        fields='__all__'
        
