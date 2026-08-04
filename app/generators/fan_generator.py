from app.models.team import FanCulture
from app.data.fans import FAN_REPUTATIONS, SUPPORTER_GROUPS, ATMOSPHERES

class FanGenerator:
    def __init__(self, random_service):
        self.random = random_service

    def generate(self, club_name: str, stadium_capacity: int) -> FanCulture:

        min_attendance = int(stadium_capacity * 0.50)
        attendance = self.random.integer(min_attendance, stadium_capacity)

        return FanCulture(
            supporter_name=self.random.choice(SUPPORTER_GROUPS),
            atmosphere=self.random.choice(ATMOSPHERES),
            average_attendance=attendance,
            reputation=self.random.choice(FAN_REPUTATIONS),
        )