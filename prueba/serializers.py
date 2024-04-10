from rest_framework import serializers
from .models import Feature, Comment


class FeatureSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField() 
    attributes = serializers.SerializerMethodField()       

    class Meta:
        model = Feature
        fields = (
            "id",
            "type",
            "attributes",
            "links",
        )
    
    def get_links(self, obj):
        return {
            "external_url": obj.external_url,
        }
    
    def get_attributes(self, obj):
        return {
            "external_id": obj.external_id,
            "magnitude": obj.magnitude,
            "place": obj.place,
            "time": obj.time,
            "tsunami": obj.tsunami,
            "mag_type": obj.mag_type,
            "title": obj.title,
            "coordinates": {
                "longitude": obj.longitude,
                "latitude": obj.latitude,
            }
        }

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "body",
        )
