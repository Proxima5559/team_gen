from app.data.positions import POSITION_KIT_NUMBERS, SQUAD_LIMITS
from app.data.formation import FORMATIONS
from app.data.countries import COUNTRY_TO_LOCALE, COUNTRY_TO_NATIONALITY, COUNTRY_TO_LEAGUES, DEFAULT_TIER, LEAGUE_TIERS
from app.generators.manager_generator import ManagerGenerator
from app.generators.player_generator import PlayerGenerator
from app.generators.stadium_generator import StadiumGenerator
from app.models.team import Team
from app.services.formation_service import FormationService
from app.services.random_service import RandomService
from app.generators.history_generator import HistoryGenerator
from app.generators.identity_generator import IdentityGenerator
from app.generators.fan_generator import FanGenerator
from app.generators.jersey_generator import JerseyGenerator


class TeamGenerator:
    def __init__(
        self, 
        random_service: RandomService,
        formation_service: FormationService,
        manager_generator: ManagerGenerator,
        player_generator: PlayerGenerator,
        stadium_generator: StadiumGenerator,
        history_generator: HistoryGenerator,
        identity_generator: IdentityGenerator,
        fan_generator: FanGenerator,
        jersey_generator: JerseyGenerator,
    ):
        self.random = random_service
        self.formation_service = formation_service
        self.manager_generator = manager_generator
        self.player_generator = player_generator
        self.stadium_generator = stadium_generator
        self.history_generator = history_generator
        self.identity_generator = identity_generator
        self.fan_generator = fan_generator
        self.jersey_generator = jersey_generator
    

    def _generate_squad(
        self,
        country: str,
        formation: str,
        player_countries: dict[str, int] | None = None,
        overall_range: tuple[int, int] = (60, 94),
    ) -> list:
        used_numbers = set()

        def get_next_number(position: str, preferred: int | None = None) -> int:
            min_num, max_num = POSITION_KIT_NUMBERS.get(position, (1, 99))

            if preferred and preferred not in used_numbers and min_num <= preferred <= max_num:
                used_numbers.add(preferred)
                return preferred

            attempts = 0
            while attempts < 20:
                num = self.random.integer(min_num, max_num)
                if num not in used_numbers:
                    used_numbers.add(num)
                    return num
                attempts += 1
            
            for num in range(min_num, max_num + 1):
                if num not in used_numbers:
                    used_numbers.add(num)
                    return num
            
            for num in range(1, 100):
                if num not in used_numbers:
                    used_numbers.add(num)
                    return num
            
            return 99

        starting_positions = self.formation_service.get_positions(formation)

        position_counts = {}
        for pos in starting_positions:
            position_counts[pos] = position_counts.get(pos, 0) + 1

        target_position_counts = {
            pos: self.random.integer(min_needed, max_needed)
            for pos, (min_needed, max_needed) in SQUAD_LIMITS.items()
        }

        depth_positions = []
        for pos, target_count in target_position_counts.items():
            existing_count = position_counts.get(pos, 0)
            needed_depth = max(0, target_count - existing_count)
            for _ in range(needed_depth):
                depth_positions.append(pos)

        all_positions = starting_positions + depth_positions
        squad_size = len(all_positions)

        nationalities: list[str] = []
        for pick_country, count in (player_countries or {}).items():
            nationalities.extend([pick_country] * count)
        nationalities = nationalities[:squad_size]

        remaining = squad_size - len(nationalities)
        nationalities.extend(
            self.random.choice(list(COUNTRY_TO_LOCALE.keys())) for _ in range(remaining)
        )
        self.random.shuffle(nationalities)

        starting_players = [
            self.player_generator.generate(
                country=nationalities[idx - 1],
                position=pos,
                kit_number=get_next_number(pos, 1 if pos == "GK" else idx),
                overall_range=overall_range,
            )
            for idx, pos in enumerate(starting_positions, start=1)
        ]

        depth_players = [
            self.player_generator.generate(
                country=nationalities[len(starting_positions) + i],
                position=pos,
                kit_number=get_next_number(pos),
                overall_range=overall_range,
            )
            for i, pos in enumerate(depth_positions)
        ]

        return starting_players + depth_players
    
    def generate(self, request) -> Team:
        country = request.country or self.random.choice(list(COUNTRY_TO_NATIONALITY.keys()))
        league = request.league or self.random.choice(COUNTRY_TO_LEAGUES[country])
        identity = self.identity_generator.generate(country)
        
        club_name = request.club_name or identity.club_name
        playing_style = request.playing_style or self.random.choice([
            "Balanced", "Possession", "Counter-Attack", "Pressing", "Direct"
        ])

        tier = LEAGUE_TIERS.get(league, DEFAULT_TIER)
        tier_min_budget, tier_max_budget = tier["budget"]
        tier_min_ovr, tier_max_ovr = tier["overall"]
        capacity_range = tier.get("capacity")
        
        budget = request.budget or self.random.integer(tier_min_budget, tier_max_budget)
        formation = request.formation or self.random.choice(list(FORMATIONS.keys()))

        overall_range = (
            request.min_strength if request.min_strength is not None else tier_min_ovr,
            request.max_strength if request.max_strength is not None else tier_max_ovr,
        )

        manager = self.manager_generator.generate(
            country=country,
            formation=formation,
            style=playing_style,
            name=request.manager_name,
        )

        stadium = self.stadium_generator.generate(
            country=country,
            capacity_range=capacity_range,
            name=request.stadium_name,
        )

        players = self._generate_squad(
            country=country,
            formation=formation,
            overall_range=overall_range
        )

        history = self.history_generator.generate(founded=identity.founded)
        fans = self.fan_generator.generate(
            club_name=club_name,
            stadium_capacity=stadium.capacity,
        )

        jerseys = self.jersey_generator.generate(
            primary_color=identity.primary_color,
            secondary_color=identity.secondary_color,
        )


        return Team(
            name=club_name,
            country=country,
            league=league,
            budget=budget,
            formation=formation,
            playing_style=playing_style,
            manager=manager,
            stadium=stadium,
            players=players,
            identity=identity,
            history=history,
            fans=fans,
            jerseys=jerseys
        )