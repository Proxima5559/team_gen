from app.data.countries import COUNTRY_TO_NATIONALITY
from app.generators.fan_generator import FanGenerator
from app.generators.history_generator import HistoryGenerator
from app.generators.identity_generator import IdentityGenerator
from app.generators.jersey_generator import JerseyGenerator
from app.generators.manager_generator import ManagerGenerator
from app.generators.player_generator import PlayerGenerator
from app.generators.stadium_generator import StadiumGenerator
from app.generators.team_generator import TeamGenerator
from app.services.formation_service import FormationService
from app.services.nationality_service import NationalityService
from app.services.random_service import RandomService
from app.services.valuation_service import ValuationService
from app.services.attribute_service import AttributeService

def get_team_generator() -> TeamGenerator:
    random_service = RandomService()
    nationality_service = NationalityService(COUNTRY_TO_NATIONALITY)
    formation_service = FormationService()
    valuation_service = ValuationService(random_service=random_service)
    attribute_service = AttributeService(random_service=random_service)

    return TeamGenerator(
        random_service=random_service,
        formation_service=formation_service,
        manager_generator=ManagerGenerator(
            random_service=random_service,
            nationality_service=nationality_service,
        ),
        player_generator=PlayerGenerator(
            random_service=random_service,
            nationality_service=nationality_service,
            valuation_service=valuation_service,     
            attribute_service=attribute_service,
        ),
        stadium_generator=StadiumGenerator(random_service=random_service),
        history_generator=HistoryGenerator(random_service=random_service),
        identity_generator=IdentityGenerator(random_service=random_service),
        fan_generator=FanGenerator(random_service=random_service),
        jersey_generator=JerseyGenerator(random_service=random_service),
    )