from rest_framework import serializers
from webapp.models import STATUS_CHOICES, Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200, required=True)
    text = serializers.CharField(max_length=3000, required=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.ChoiceField(choices=STATUS_CHOICES, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()
            return instance


class DetailSerializer(serializers.ModelSerializer):

    tags = serializers.SlugRelatedField(slug_field='name', read_only=True)
    author = serializers.SlugField(read_only=True)

    class Meta:
        model = Article
        exclude = ''

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "text")

    def create(self, validated_data):
        article = Article.objects.update_or_create(
            title={"title": validated_data.get("title")},
            text={"text":validated_data.get("text")}
        )
        return article



