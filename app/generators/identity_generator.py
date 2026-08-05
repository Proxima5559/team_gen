from mimesis import Address
from mimesis.locales import Locale

from app.data.club_names import CLUB_NAME_BLUEPRINTS
from app.models.team import ClubIdentity
from app.data.colors import COLOR_PALETTES
from app.data.fans import NICKNAMES, MOTTOS, MASCOTS
from app.services.random_service import RandomService
from app.services.text_sanitizer import TextSanitizer


class IdentityGenerator:
    def __init__(self, random_service: RandomService):
        self.random = random_service

    def generate(self, country: str) -> ClubIdentity:
        current_year = 2026
        founded = self.random.integer(1870, current_year - 1)

        home_palette = self.random.choice(COLOR_PALETTES)
        primary_color = home_palette["primary"]
        secondary_color = home_palette["secondary"]

        raw_club_name = self._generate_club_name(country)

        club_name = TextSanitizer.to_latin(raw_club_name)
        nickname = self.random.choice(NICKNAMES)

        return ClubIdentity(
            founded=founded,
            nickname=nickname,
            club_name=club_name,
            motto=self.random.choice(MOTTOS),
            primary_color=primary_color,
            secondary_color=secondary_color,
            mascot=self.random.choice(MASCOTS),
        )


    def _generate_club_name(self, country: str) -> str:
        from app.data.countries import COUNTRY_TO_LOCALE
        
        locale = COUNTRY_TO_LOCALE.get(country)
        if not locale:
            locale = Locale.EN  
        
        address = Address(locale)
        city = address.city()
        
        blueprints = CLUB_NAME_BLUEPRINTS.get(country)
        if not blueprints:
            blueprints = [
                "{city} United",
                "{city} City",
                "FC {city}",
                "Dynamo {city}",
                "{city} Athletic",
                "{city} Rangers"
            ]
        
        blueprint = self.random.choice(blueprints)
        return blueprint.format(city=city)