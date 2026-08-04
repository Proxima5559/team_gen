from app.services.random_service import RandomService


class ValuationService:

    def __init__(self, random_service: RandomService):
        self.random = random_service

    def calculate_player_value(self, age: int, overall: int, potential: int) -> int:
        base_value = int(200_000 * (1.17 ** (overall - 60)))

        age_factor = max(0.2, 1.2 - max(0, age - 25) * 0.1)
        potential_growth = potential - overall
        age_window = max(0, 26 - age) / 9.0
        potential_factor = 1.0 + (potential_growth * 0.12 * age_window)

        random_modifier = self.random.integer(90, 110) / 100.0
        final_value = int(base_value * age_factor * potential_factor * random_modifier)

        return max(100_000, min(180_000_000, final_value))