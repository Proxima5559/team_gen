from app.models.team import Jersey
from app.data.colors import COLORS
from app.services.random_service import RandomService


class JerseyGenerator:
    def __init__(self, random_service: RandomService):
        self.random = random_service

    def generate(self, primary_color: str, secondary_color: str) -> Jersey:
        available_colors = [c for c in COLORS if c not in (primary_color, secondary_color)]

        away_primary = self.random.choice(available_colors)
        available_colors.remove(away_primary)

        away_secondary = self.random.choice(available_colors)
        available_colors.remove(away_secondary)

        third_primary = self.random.choice(available_colors)
        available_colors.remove(third_primary)

        third_secondary = self.random.choice(available_colors)

        return Jersey(
            home_primary=primary_color,
            home_secondary=secondary_color,
            away_primary=away_primary,
            away_secondary=away_secondary,
            third_primary=third_primary,
            third_secondary=third_secondary,
        )