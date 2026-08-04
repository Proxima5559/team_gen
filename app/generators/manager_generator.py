from mimesis import Person
from app.models.manager import Manager
from app.services.random_service import RandomService
from app.services.nationality_service import NationalityService
from app.data.countries import COUNTRY_TO_LOCALE

class ManagerGenerator:
    def __init__(self, random_service: RandomService, nationality_service: NationalityService):
        self.random = random_service
        self.nationality_service = nationality_service

    def generate(self, country: str, formation: str, style: str, name: str | None = None) -> Manager:
        locale = COUNTRY_TO_LOCALE.get(country, "en")
        
        person = Person(locale=locale, seed=self.random.integer(1, 1_000_000))
        
        return Manager(
            name=name or person.full_name(),
            nationality=self.nationality_service.from_country(country),
            formation=formation,
            style=style,
        )
