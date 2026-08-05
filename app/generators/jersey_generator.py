from app.models.team import Jersey
from app.data.colors import COLOR_PALETTES
from app.services.random_service import RandomService


class JerseyGenerator:
    def __init__(self, random_service: RandomService):
        self.random = random_service

    def generate(self, primary_color: str, secondary_color: str) -> Jersey:
        available_palettes = [
            p for p in COLOR_PALETTES 
            if p["primary"] != primary_color and p["secondary"] != secondary_color
        ]

        away_palette = self.random.choice(available_palettes)
        available_palettes.remove(away_palette)

        third_palette = self.random.choice(available_palettes)

        return Jersey(
            home_primary=primary_color,
            home_secondary=secondary_color,
            away_primary=away_palette["primary"],
            away_secondary=away_palette["secondary"],
            third_primary=third_palette["primary"],
            third_secondary=third_palette["secondary"],
        )