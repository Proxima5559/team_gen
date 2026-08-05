from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender

from app.data.countries import COUNTRY_TO_LOCALE
from app.models.player import Player
from app.data.positions import (
    POSITION_BMI,
    POSITION_HEIGHTS,
    POSITIONS
)
from app.services.random_service import RandomService
from app.services.nationality_service import NationalityService
from app.services.text_sanitizer import TextSanitizer
from app.services.valuation_service import ValuationService
from app.services.attribute_service import AttributeService

class PlayerGenerator:
    def __init__(
        self,
        random_service: RandomService,
        nationality_service: NationalityService,
        valuation_service: ValuationService,
        attribute_service: AttributeService,
    ):
        self.random = random_service
        self.nationality_service = nationality_service
        self.valuation_service = valuation_service
        self.attribute_service = attribute_service

    def _get_person_generator(self, country: str) -> Person:
        locale = COUNTRY_TO_LOCALE.get(country, Locale.EN)
        return Person(locale=locale, seed=self.random.integer(1, 1_000_000))

    def generate(self, country: str, position: str, kit_number: int = 1, overall_range: tuple[int, int] = (60, 94)) -> Player:
        pos_code = position if position in POSITIONS else "CM"
        person = self._get_person_generator(country)

        raw_name = person.full_name(gender=Gender.MALE)
        latin_name = TextSanitizer.to_latin(raw_name)
    
        age = self.random.integer(17, 40)
        low, high = sorted(overall_range)
        overall = self.random.integer(low, high)
        has_growth = 1 if age < 28 else 0
        potential = min(99, overall + self.random.integer(0, 12) * has_growth)

        market_value = self.valuation_service.calculate_player_value(age, overall, potential)
        attributes = self.attribute_service.generate_player_attributes(pos_code, overall, physical=0, defending=0)

        height_min, height_max = POSITION_HEIGHTS.get(pos_code, (175, 185))
        height_cm = self.random.integer(height_min, height_max)

        bmi_min, bmi_max = POSITION_BMI.get(pos_code, (22, 25))
        bmi = self.random.float(bmi_min, bmi_max)
        weight_kg = int(bmi * ((height_cm / 100) ** 2))

        return Player(
            name=latin_name,
            kit_number=kit_number,
            age=age,
            nationality=self.nationality_service.from_country(country),
            position=pos_code,
            overall=overall,
            potential=potential,
            market_value=market_value,
            preferred_foot=self.random.weighted_choice(["Left", "Right", "Both"], weights=[20, 75, 5]),
            height_cm=height_cm,
            weight_kg=weight_kg,
            **attributes,  
        )