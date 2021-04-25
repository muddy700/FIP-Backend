from ninja import NinjaAPI
from users.api import router as filter_routers

api = NinjaAPI()

api.add_router("/filter/", filter_routers)
