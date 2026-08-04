from app.data.positions import POSITION_ATTRIBUTES
from app.services.random_service import RandomService


class AttributeService:

    def __init__(self, random_service: RandomService):
        self.random = random_service

    def generate_base_attribute(self, overall: int, weight: float) -> int:
        base = overall * weight
        variation = self.random.integer(-5, 5)
        stat = int(base + variation)
        return max(20, min(99, stat))

    def generate_player_attributes(self, pos_code: str, overall: int, physical: int, defending: int) -> dict:
        weights = POSITION_ATTRIBUTES.get(
            pos_code,
            {
                "pace": 0.6,
                "shooting": 0.6,
                "passing": 0.6,
                "defending": 0.6,
                "physical": 0.6,
                "dribbling": 0.6,
                "goalkeeping": 0.1,
            },
        )

        pace = self.generate_base_attribute(overall, weights.get("pace", 0.6))
        shooting = self.generate_base_attribute(overall, weights.get("shooting", 0.6))
        passing = self.generate_base_attribute(overall, weights.get("passing", 0.6))
        defending_stat = self.generate_base_attribute(overall, weights.get("defending", 0.6))
        physical_stat = self.generate_base_attribute(overall, weights.get("physical", 0.6))
        dribbling = self.generate_base_attribute(overall, weights.get("dribbling", 0.6))
        goalkeeping = self.generate_base_attribute(overall, weights.get("goalkeeping", 0.1))

        return {
            "pace": pace,
            "shooting": shooting,
            "passing": passing,
            "defending": defending_stat,
            "physical": physical_stat,
            "dribbling": dribbling,
            "goalkeeping": goalkeeping,
            "aggression": max(20, min(99, overall + self.random.integer(-10, 10))),
            "stamina": max(20, min(99, overall + self.random.integer(-8, 8))),
            "strength": max(20, min(99, physical_stat + self.random.integer(-5, 5))),
            "jumping": max(20, min(99, physical_stat + self.random.integer(-8, 8))),
            "heading": max(20, min(99, defending_stat + self.random.integer(-10, 10))),
        }