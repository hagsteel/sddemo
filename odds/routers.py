from swampdragon import route_handler
from swampdragon.route_handler import BaseModelPublisherRouter
from .models import Odds
from .serializers import OddsSerializer

# Started building this demo at 13:15
class OddsRouter(BaseModelPublisherRouter):
    model = Odds
    route_name = 'odds-route'
    serializer_class = OddsSerializer

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


route_handler.register(OddsRouter)
