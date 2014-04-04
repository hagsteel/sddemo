from swampdragon.serializers.django_model_serializer import DjangoModelSerializer


class OddsSerializer(DjangoModelSerializer):
    model = 'odds.Odds'
    publish_fields = ['market', 'odds']
