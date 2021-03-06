from rest_framework import serializers
from .models import Article

# ======================= serializer ============================
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.CharField(max_length=100)
#     date = serializers.DateTimeField()
    
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.CharField(max_length=100)
#         instance.author = validated_data.CharField(max_length=100)
#         instance.email = validated_data.CharField(max_length=100)
#         instance.date = validated_data.DateTimeField()
#         instance.save()
#         return instance


# ====================== MODEL SERIALIZER ========================

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']