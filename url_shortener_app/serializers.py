from rest_framework import serializers
from url_shortener_app.models import UrlModel


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlModel
        fields = '__all__'