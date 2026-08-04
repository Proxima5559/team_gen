from mimesis import Address
from mimesis.locales import Locale
from app.models.stadium import Stadium
from app.services.random_service import RandomService
from app.data.countries import COUNTRY_TO_LOCALE, COUNTRY_TO_CAPACITY, LEAGUE_TIERS

class StadiumGenerator:
    def __init__(self, random_service: RandomService):
        self.random = random_service
        
    def generate(self, country: str, capacity_range: tuple[int, int] | None = None, name: str | None = None) -> Stadium:
        locale = COUNTRY_TO_LOCALE.get(country, Locale.EN)
        address = Address(locale=locale, seed=self.random.integer(1, 1_000_000))

        min_cap, max_cap = capacity_range or COUNTRY_TO_CAPACITY.get(country, (8000, 85000))
        
        return Stadium(
            name=name or f"{address.street_name()} Stadium",
            city=address.city(),
            capacity=self.random.integer(min_cap, max_cap),
        )