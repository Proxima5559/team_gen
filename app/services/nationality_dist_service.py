
from app.data.countries import COUNTRY_TO_CHANCE, COUNTRY_TO_NATIONALITY, LEAGUE_NATIONALITY_MODIFIERS
from app.services.random_service import RandomService


class NationalityDistributionService:
    def __init__(self, random_service: RandomService):
        self.random = random_service

    def get_weights(
        self,
        country: str,
        league: str,
    ) -> tuple[list[str], list[float]]:

        countries = list(COUNTRY_TO_CHANCE.keys())

        weights = []

        league_modifiers = (
            LEAGUE_NATIONALITY_MODIFIERS
            .get(country, {})
            .get(league, {})
        )

        for player_country in countries:
            nationality = COUNTRY_TO_NATIONALITY[player_country]

            base_chance = COUNTRY_TO_CHANCE[player_country]

            modifier = league_modifiers.get(nationality, 1.0)

            weights.append(base_chance * modifier)

        return countries, weights

    def generate(
        self,
        country: str,
        league: str,
    ) -> str:

        countries, weights = self.get_weights(
            country=country,
            league=league,
        )

        return self.random.weighted_choice(
            countries,
            weights=weights,
        )