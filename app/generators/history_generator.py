from app.models.team import History
from app.data.fans import HISTORY_EVENTS
from app.services.random_service import RandomService

class HistoryGenerator:
    def __init__(self, random_service: RandomService):
        self.random = random_service

    def generate_founding_year(self) -> int:
        eras = [
            (1870, 1899),
            (1900, 1949),
            (1950, 1999),
            (2000, 2026),
        ]
        weights = [5, 15, 40, 40]

        selected_era = self.random.weighted_choice(eras, weights=weights)
        return self.random.integer(selected_era[0], selected_era[1])

    def generate(self, founded: int | None = None) -> History:
        if founded is None:
            founded = self.generate_founding_year()

        current_year = 2026
        club_age = current_year - founded

        available_events = list(HISTORY_EVENTS)

        if club_age < 100:
            available_events = [t for t in available_events if "centennial" not in t.lower()]

        max_milestones = min(self.random.integer(1, 4), max(1, club_age // 5))
        
        valid_years = [
            y for y in range(founded + 1, current_year + 1)
            if not (1914 <= y <= 1918) and not (1939 <= y <= 1945)
        ]

        milestone_data = []
        selected_years = set()

        for _ in range(max_milestones):
            if not valid_years or not available_events:
                break
            
            event_template = self.random.choice(available_events)
            available_events.remove(event_template)

            if "centennial" in event_template.lower():
                centennial_year = founded + 100
                if centennial_year <= current_year:
                    year = centennial_year
                else:
                    continue
            else:
                possible_years = [y for y in valid_years if y not in selected_years]
                if not possible_years:
                    break
                year = self.random.choice(possible_years)

            selected_years.add(year)
            milestone_data.append((year, event_template))

        milestone_data.sort(key=lambda x: x[0])

        milestones = [f"Club founded in {founded}."]
        for year, template in milestone_data:
            milestones.append(template.format(year=year))

        return History(founded=founded, milestones=milestones)